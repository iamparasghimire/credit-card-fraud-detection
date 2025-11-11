"""
Quick start example for credit card fraud detection.
Run this to get started with the fraud detection system.
"""

import os
import sys
from data_loader import load_data, preprocess_data, analyze_data
from model_trainer import ModelTrainer


def main():
    print("=" * 60)
    print("🚨 Credit Card Fraud Detection - Quick Start")
    print("=" * 60)
    
    # Check if dataset exists
    if not os.path.exists('creditcard.csv'):
        print("\n❌ Dataset not found!")
        print("Please download creditcard.csv from Kaggle:")
        print("   https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud")
        print("\nPlace the file in the project root directory.")
        return
    
    print("\n1️⃣ Loading and analyzing data...")
    data = load_data('creditcard.csv')
    stats = analyze_data(data)
    
    print(f"   Dataset shape: {stats['shape']}")
    print(f"   Total transactions: {stats['shape'][0]:,}")
    print(f"   Normal transactions: {stats['normal_percentage']:.2f}%")
    print(f"   Fraudulent transactions: {stats['fraud_percentage']:.2f}%")
    print(f"   Missing values: {stats['null_values']}")
    
    print("\n2️⃣ Preprocessing data...")
    X_train, X_test, y_train, y_test, scaler = preprocess_data(data)
    print(f"   Training set size: {X_train.shape[0]}")
    print(f"   Test set size: {X_test.shape[0]}")
    print(f"   Features: {X_train.shape[1]}")
    
    print("\n3️⃣ Training all models (this may take a few minutes)...")
    trainer = ModelTrainer()
    results = trainer.train_all_models(X_train, y_train, cv=5)
    
    print("\n   Model Training Results:")
    print("   " + "-" * 50)
    for _, row in results.iterrows():
        print(f"   {row['model']:.<30} {row['best_score']:.4f}")
    
    print("\n4️⃣ Evaluating best model...")
    metrics = trainer.evaluate_best_model(X_test, y_test)
    
    print(f"\n   Model: {metrics['model_name'].replace('_', ' ').title()}")
    print(f"   Accuracy:  {metrics['accuracy']*100:.2f}%")
    print(f"   Precision: {metrics['precision']*100:.2f}%")
    print(f"   Recall:    {metrics['recall']*100:.2f}%")
    print(f"   F1 Score:  {metrics['f1']:.4f}")
    if 'roc_auc' in metrics:
        print(f"   ROC-AUC:   {metrics['roc_auc']:.4f}")
    
    print("\n5️⃣ Saving model...")
    os.makedirs('models', exist_ok=True)
    trainer.save_best_model('models/best_fraud_model.pkl')
    print("   ✅ Model saved to models/best_fraud_model.pkl")
    
    print("\n" + "=" * 60)
    print("✨ Quick start completed!")
    print("=" * 60)
    print("\nNext steps:")
    print("  📊 Run Streamlit GUI: streamlit run app.py")
    print("  🔌 Run Flask API: python api.py")
    print("  🔄 Batch predictions: python batch_predict.py --input input.csv --output predictions.csv")
    print("\n" + "=" * 60)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
