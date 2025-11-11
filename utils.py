"""
Utilities module for the fraud detection system.
"""

import os
import pickle
import json
from datetime import datetime

def create_directories():
    """Create necessary directories if they don't exist."""
    directories = ['models', 'logs', 'data', 'results']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def save_json(data: dict, filepath: str):
    """Save dictionary as JSON file."""
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def load_json(filepath: str) -> dict:
    """Load JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_timestamp():
    """Get current timestamp as string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_percentage(value: float) -> str:
    """Format value as percentage string."""
    return f"{value * 100:.2f}%"

def get_model_info() -> dict:
    """Get information about all available models."""
    models_info = {
        'logistic_regression': {
            'name': 'Logistic Regression',
            'type': 'Linear',
            'speed': 'Very Fast',
            'accuracy': 'Good'
        },
        'svm': {
            'name': 'Support Vector Machine',
            'type': 'Non-linear',
            'speed': 'Medium',
            'accuracy': 'Excellent'
        },
        'decision_tree': {
            'name': 'Decision Tree',
            'type': 'Tree-based',
            'speed': 'Very Fast',
            'accuracy': 'Good'
        },
        'random_forest': {
            'name': 'Random Forest',
            'type': 'Ensemble',
            'speed': 'Fast',
            'accuracy': 'Excellent'
        },
        'naive_bayes': {
            'name': 'Gaussian Naive Bayes',
            'type': 'Probabilistic',
            'speed': 'Very Fast',
            'accuracy': 'Fair'
        },
        'knn': {
            'name': 'K-Nearest Neighbors',
            'type': 'Distance-based',
            'speed': 'Medium',
            'accuracy': 'Good'
        }
    }
    return models_info
