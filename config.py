"""
Configuration settings for the fraud detection system.
"""

# Model Configuration
MODEL_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
    'cv_folds': 5,
    'use_undersampling': True,
    'scaler_type': 'StandardScaler'
}

# API Configuration
API_CONFIG = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': False,
    'timeout': 300
}

# Streamlit Configuration
STREAMLIT_CONFIG = {
    'page_title': 'Credit Card Fraud Detection',
    'layout': 'wide',
    'theme': 'light'
}

# Model Paths
MODEL_PATHS = {
    'best_model': 'models/best_fraud_model.pkl',
    'scaler': 'models/scaler.pkl',
    'history': 'models/training_history.pkl'
}

# Performance Thresholds
THRESHOLDS = {
    'fraud_probability': 0.5,
    'min_accuracy': 0.95,
    'min_precision': 0.90
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'logs/fraud_detection.log'
}
