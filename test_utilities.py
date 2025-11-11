"""
Testing utilities and test case generators.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from typing import Tuple

class TestDataGenerator:
    """Generate synthetic test data for model validation."""
    
    @staticmethod
    def generate_synthetic_data(
        n_samples: int = 1000,
        n_features: int = 30,
        n_informative: int = 20,
        n_redundant: int = 5,
        weights: Tuple[float, float] = (0.98, 0.02),
        random_state: int = 42
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate synthetic fraud detection dataset.
        
        Args:
            n_samples: Number of samples
            n_features: Total features
            n_informative: Informative features
            n_redundant: Redundant features
            weights: Class distribution (normal, fraud)
            random_state: Random seed
        
        Returns:
            X (features), y (labels)
        """
        X, y = make_classification(
            n_samples=n_samples,
            n_features=n_features,
            n_informative=n_informative,
            n_redundant=n_redundant,
            weights=weights,
            random_state=random_state
        )
        return X, y
    
    @staticmethod
    def generate_test_cases(n_cases: int = 10) -> pd.DataFrame:
        """Generate test cases for API testing."""
        X, _ = TestDataGenerator.generate_synthetic_data(n_samples=n_cases)
        df = pd.DataFrame(X)
        df.columns = [f'feature_{i}' for i in range(df.shape[1])]
        return df


class ModelTester:
    """Test suite for model validation."""
    
    @staticmethod
    def test_model_output_shape(model, X_test: np.ndarray, expected_shape: Tuple):
        """Test if model output shape is correct."""
        y_pred = model.predict(X_test)
        assert y_pred.shape == expected_shape, f"Expected {expected_shape}, got {y_pred.shape}"
        return True
    
    @staticmethod
    def test_prediction_range(model, X_test: np.ndarray, min_val: float = 0, max_val: float = 1):
        """Test if predictions are in expected range."""
        y_pred = model.predict_proba(X_test) if hasattr(model, 'predict_proba') else model.predict(X_test)
        assert np.all(y_pred >= min_val) and np.all(y_pred <= max_val), \
            f"Predictions out of range [{min_val}, {max_val}]"
        return True
    
    @staticmethod
    def test_model_consistency(model, X_test: np.ndarray, runs: int = 3):
        """Test if model produces consistent predictions."""
        predictions = []
        for _ in range(runs):
            pred = model.predict(X_test)
            predictions.append(pred)
        
        # Check if all predictions are identical
        for pred in predictions[1:]:
            assert np.array_equal(predictions[0], pred), "Predictions are not consistent"
        return True
    
    @staticmethod
    def test_model_handles_nan(model, X_test: np.ndarray):
        """Test if model handles NaN values gracefully."""
        X_test_with_nan = X_test.copy()
        X_test_with_nan[0, 0] = np.nan
        
        try:
            model.predict(X_test_with_nan)
            return False  # Should have raised error
        except Exception:
            return True  # Expected behavior


class ValidationReport:
    """Generate validation reports."""
    
    @staticmethod
    def generate_test_report(test_results: dict) -> str:
        """Generate formatted test report."""
        report = "\n" + "="*60 + "\n"
        report += "VALIDATION TEST REPORT\n"
        report += "="*60 + "\n"
        
        for test_name, passed in test_results.items():
            status = "✓ PASS" if passed else "✗ FAIL"
            report += f"{test_name:<40} {status}\n"
        
        total = len(test_results)
        passed = sum(1 for v in test_results.values() if v)
        report += "="*60 + "\n"
        report += f"Total: {passed}/{total} tests passed\n"
        report += "="*60 + "\n"
        
        return report
