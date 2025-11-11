"""
Flask API for credit card fraud detection.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import os
import json
from data_loader import load_data, preprocess_data, analyze_data
from model_trainer import ModelTrainer


app = Flask(__name__)
CORS(app)

# Global variables
trainer = ModelTrainer()
scaler = None
model_path = 'models/best_fraud_model.pkl'


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok', 'message': 'API is running'})


@app.route('/api/train', methods=['POST'])
def train_model():
    """
    Train the fraud detection model.
    
    Expected JSON:
    {
        "data_path": "path/to/creditcard.csv"
    }
    """
    try:
        data_path = request.json.get('data_path', 'creditcard.csv')
        
        # Load and preprocess data
        data = load_data(data_path)
        X_train, X_test, y_train, y_test, scaler_obj = preprocess_data(data)
        
        global scaler
        scaler = scaler_obj
        
        # Train all models
        results = trainer.train_all_models(X_train, y_train)
        
        # Evaluate best model
        metrics = trainer.evaluate_best_model(X_test, y_test)
        
        # Save best model
        os.makedirs('models', exist_ok=True)
        trainer.save_best_model(model_path)
        
        return jsonify({
            'status': 'success',
            'message': 'Model trained successfully',
            'best_model': trainer.best_model_name,
            'metrics': {
                'accuracy': float(metrics['accuracy']),
                'precision': float(metrics['precision']),
                'recall': float(metrics['recall']),
                'f1': float(metrics['f1']),
                'roc_auc': float(metrics.get('roc_auc', 0))
            },
            'all_models': results.to_dict(orient='records')
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Make predictions on transaction data.
    
    Expected JSON:
    {
        "transaction": [list of 30 features]
    }
    or
    {
        "transactions": [[features], [features], ...]
    }
    """
    try:
        if not os.path.exists(model_path):
            return jsonify({
                'status': 'error', 
                'message': 'Model not trained yet. Please train the model first.'
            }), 400
        
        # Load model if not already loaded
        if not trainer.best_model:
            trainer.load_model(model_path)
        
        data = request.json
        
        # Handle single transaction
        if 'transaction' in data:
            X = np.array([data['transaction']])
        # Handle multiple transactions
        elif 'transactions' in data:
            X = np.array(data['transactions'])
        else:
            return jsonify({'status': 'error', 'message': 'Invalid input format'}), 400
        
        # Standardize using saved scaler
        if scaler is not None:
            X = scaler.transform(X)
        
        predictions, probabilities = trainer.predict(X)
        
        results = []
        for i, pred in enumerate(predictions):
            result = {
                'transaction_id': i,
                'is_fraud': bool(pred),
                'fraud_probability': float(probabilities[i][1]) if probabilities is not None else None
            }
            results.append(result)
        
        return jsonify({
            'status': 'success',
            'predictions': results if len(results) > 1 else results[0]
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/api/data-stats', methods=['POST'])
def data_stats():
    """
    Get statistics about the dataset.
    
    Expected JSON:
    {
        "data_path": "path/to/creditcard.csv"
    }
    """
    try:
        data_path = request.json.get('data_path', 'creditcard.csv')
        data = load_data(data_path)
        stats = analyze_data(data)
        
        return jsonify({
            'status': 'success',
            'stats': stats
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/api/model-info', methods=['GET'])
def model_info():
    """Get information about the trained model."""
    if not trainer.best_model:
        return jsonify({
            'status': 'error',
            'message': 'No model trained yet'
        }), 400
    
    return jsonify({
        'status': 'success',
        'model_name': trainer.best_model_name,
        'model_params': trainer.best_model.get('best_params', {})
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
