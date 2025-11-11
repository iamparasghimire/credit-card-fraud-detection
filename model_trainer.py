"""
Model training and evaluation utilities for credit card fraud detection.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                            f1_score, confusion_matrix, classification_report, roc_auc_score)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import joblib
import os


class ModelTrainer:
    """Train and evaluate multiple models for fraud detection."""
    
    def __init__(self):
        """Initialize model configurations."""
        self.models = {
            'logistic_regression': {
                'model': LogisticRegression(max_iter=1000),
                'params': {'solver': ['liblinear']}
            },
            'svm': {
                'model': SVC(probability=True),
                'params': {'kernel': ['rbf', 'linear'], 'C': [10, 15, 20]}
            },
            'decision_tree': {
                'model': DecisionTreeClassifier(),
                'params': {'criterion': ['gini', 'entropy']}
            },
            'random_forest': {
                'model': RandomForestClassifier(),
                'params': {'criterion': ['gini', 'entropy'], 'n_estimators': [50, 100]}
            },
            'naive_bayes': {
                'model': GaussianNB(),
                'params': {}
            },
            'knn': {
                'model': KNeighborsClassifier(),
                'params': {'n_neighbors': [5, 10, 15]}
            }
        }
        self.results = []
        self.best_model = None
        self.best_model_name = None
        
    def train_all_models(self, X_train, y_train, cv: int = 5) -> pd.DataFrame:
        """
        Train all models using GridSearchCV.
        
        Args:
            X_train: Training features
            y_train: Training labels
            cv: Number of cross-validation folds
        
        Returns:
            DataFrame with model results
        """
        self.results = []
        
        for model_name, config in self.models.items():
            print(f"Training {model_name}...")
            
            if config['params']:  # If there are hyperparameters to tune
                clf = GridSearchCV(config['model'], config['params'], cv=cv, n_jobs=-1)
            else:  # No hyperparameters to tune
                clf = config['model']
            
            clf.fit(X_train, y_train)
            
            # Get best model and score
            if hasattr(clf, 'best_score_'):
                best_score = clf.best_score_
                best_params = clf.best_params_
                best_estimator = clf.best_estimator_
            else:
                best_score = clf.score(X_train, y_train)
                best_params = {}
                best_estimator = clf
            
            self.results.append({
                'model': model_name,
                'best_score': best_score,
                'best_params': best_params,
                'estimator': best_estimator
            })
            
            # Track best model
            if not self.best_model or best_score > self.best_model['best_score']:
                self.best_model = self.results[-1]
                self.best_model_name = model_name
        
        return self._results_to_dataframe()
    
    def _results_to_dataframe(self) -> pd.DataFrame:
        """Convert results to DataFrame."""
        df_results = pd.DataFrame([
            {'model': r['model'], 'best_score': r['best_score'], 'best_params': r['best_params']}
            for r in self.results
        ])
        return df_results.sort_values('best_score', ascending=False).reset_index(drop=True)
    
    def evaluate_best_model(self, X_test, y_test) -> dict:
        """
        Evaluate the best model on test data.
        
        Args:
            X_test: Test features
            y_test: Test labels
        
        Returns:
            Dictionary with evaluation metrics
        """
        if not self.best_model:
            raise ValueError("No model trained yet. Call train_all_models first.")
        
        model = self.best_model['estimator']
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
        
        metrics = {
            'model_name': self.best_model_name,
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred),
            'confusion_matrix': confusion_matrix(y_test, y_pred).tolist(),
            'classification_report': classification_report(y_test, y_pred)
        }
        
        if y_pred_proba is not None:
            metrics['roc_auc'] = roc_auc_score(y_test, y_pred_proba)
        
        return metrics
    
    def predict(self, X) -> tuple:
        """
        Make predictions with the best model.
        
        Args:
            X: Features to predict
        
        Returns:
            Tuple of (predictions, probabilities)
        """
        if not self.best_model:
            raise ValueError("No model trained yet. Call train_all_models first.")
        
        model = self.best_model['estimator']
        predictions = model.predict(X)
        probabilities = None
        
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(X)
        
        return predictions, probabilities
    
    def save_best_model(self, filepath: str):
        """Save the best model to disk."""
        if not self.best_model:
            raise ValueError("No model trained yet.")
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
        joblib.dump(self.best_model['estimator'], filepath)
    
    def load_model(self, filepath: str):
        """Load a saved model from disk."""
        model = joblib.load(filepath)
        self.best_model = {'estimator': model}
        self.best_model_name = 'loaded_model'
        return model
    
    def get_results_dataframe(self) -> pd.DataFrame:
        """Get results as DataFrame."""
        return self._results_to_dataframe()
