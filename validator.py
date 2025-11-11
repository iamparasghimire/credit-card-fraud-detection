"""
Data validation module for fraud detection system.
"""

import pandas as pd
import numpy as np

class DataValidator:
    """Validate input data for model training and predictions."""
    
    @staticmethod
    def validate_training_data(data: pd.DataFrame) -> bool:
        """
        Validate training dataset.
        
        Args:
            data: DataFrame to validate
        
        Returns:
            True if valid, raises exception otherwise
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")
        
        if len(data) == 0:
            raise ValueError("Data cannot be empty")
        
        if 'Class' not in data.columns:
            raise ValueError("Data must have 'Class' column for labels")
        
        if data['Class'].nunique() != 2:
            raise ValueError("Class column must have exactly 2 values (0 and 1)")
        
        if data.isnull().any().any():
            raise ValueError("Data contains null values")
        
        return True
    
    @staticmethod
    def validate_prediction_data(data: np.ndarray) -> bool:
        """
        Validate prediction data.
        
        Args:
            data: Array to validate
        
        Returns:
            True if valid
        """
        if not isinstance(data, (np.ndarray, list)):
            raise TypeError("Data must be numpy array or list")
        
        if len(data) == 0:
            raise ValueError("Data cannot be empty")
        
        return True
    
    @staticmethod
    def validate_features(data: pd.DataFrame, expected_features: int = 30) -> bool:
        """
        Validate feature count.
        
        Args:
            data: DataFrame to validate
            expected_features: Expected number of features
        
        Returns:
            True if valid
        """
        actual_features = len([c for c in data.columns if c != 'Class'])
        
        if actual_features != expected_features:
            raise ValueError(
                f"Expected {expected_features} features, got {actual_features}"
            )
        
        return True
