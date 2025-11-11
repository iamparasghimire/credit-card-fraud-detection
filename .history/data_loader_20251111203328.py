"""
Data loading and preprocessing utilities for credit card fraud detection.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load credit card data from CSV file.
    
    Args:
        filepath: Path to the CSV file
    
    Returns:
        DataFrame containing credit card transactions
    """
    data = pd.read_csv(filepath)
    return data


def analyze_data(data: pd.DataFrame) -> dict:
    """
    Analyze the dataset and return statistics.
    
    Args:
        data: DataFrame to analyze
    
    Returns:
        Dictionary containing data statistics
    """
    stats = {
        'shape': data.shape,
        'null_values': data.isnull().sum().sum(),
        'class_distribution': data['Class'].value_counts().to_dict(),
        'fraud_percentage': (len(data[data['Class'] == 1]) / len(data)) * 100,
        'normal_percentage': (len(data[data['Class'] == 0]) / len(data)) * 100,
        'amount_stats': {
            'min': data['Amount'].min(),
            'max': data['Amount'].max(),
            'mean': data['Amount'].mean(),
            'median': data['Amount'].median()
        }
    }
    return stats


def preprocess_data(data: pd.DataFrame, test_size: float = 0.2, 
                   use_undersampling: bool = True, random_state: int = 40):
    """
    Preprocess data: handle imbalance and create train-test split.
    
    Args:
        data: DataFrame to preprocess
        test_size: Fraction of data for testing
        use_undersampling: Whether to use undersampling to balance classes
        random_state: Random seed for reproducibility
    
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    # Handle class imbalance using undersampling
    if use_undersampling:
        normal = data[data['Class'] == 0]
        fraud = data[data['Class'] == 1]
        
        # Sample normal transactions equal to fraud count
        normal_sampled = normal.sample(n=len(fraud), random_state=random_state)
        balanced_data = pd.concat([normal_sampled, fraud], axis=0)
    else:
        balanced_data = data
    
    # Split features and target
    X = balanced_data.drop(columns='Class', axis=1)
    y = balanced_data['Class']
    
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def get_feature_names(data: pd.DataFrame) -> list:
    """Get list of feature names excluding the target variable."""
    return [col for col in data.columns if col != 'Class']
