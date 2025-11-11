"""
Batch processing utility for fraud detection predictions.
"""

import pandas as pd
import numpy as np
import argparse
from data_loader import load_data
from model_trainer import ModelTrainer
import os


def batch_predict(input_file: str, output_file: str, model_path: str = 'models/best_fraud_model.pkl'):
    """
    Batch predict fraud on transactions from a CSV file.
    
    Args:
        input_file: Path to input CSV with transactions
        output_file: Path to save predictions
        model_path: Path to saved model
    """
    print(f"Loading model from {model_path}...")
    
    trainer = ModelTrainer()
    trainer.load_model(model_path)
    
    print(f"Loading transactions from {input_file}...")
    data = pd.read_csv(input_file)
    
    # Extract features
    feature_cols = [col for col in data.columns if col != 'Class']
    X = data[feature_cols].values
    
    print(f"Making predictions on {len(X)} transactions...")
    predictions, probabilities = trainer.predict(X)
    
    # Create results
    results = pd.DataFrame({
        'prediction': ['Fraud' if p == 1 else 'Normal' for p in predictions],
        'fraud_probability': [prob[1] if probabilities is not None else 0.0 for prob in probabilities],
        'is_fraud': predictions
    })
    
    # Add original data
    results = pd.concat([data.reset_index(drop=True), results.reset_index(drop=True)], axis=1)
    
    # Save results
    results.to_csv(output_file, index=False)
    
    print(f"Results saved to {output_file}")
    print(f"Fraud detected: {(predictions == 1).sum()} out of {len(predictions)} transactions")


def main():
    parser = argparse.ArgumentParser(description='Batch prediction for credit card fraud detection')
    parser.add_argument('--input', required=True, help='Input CSV file with transactions')
    parser.add_argument('--output', required=True, help='Output CSV file for predictions')
    parser.add_argument('--model', default='models/best_fraud_model.pkl', help='Path to saved model')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found")
        return
    
    if not os.path.exists(args.model):
        print(f"Error: Model file {args.model} not found. Please train a model first.")
        return
    
    batch_predict(args.input, args.output, args.model)


if __name__ == '__main__':
    main()
