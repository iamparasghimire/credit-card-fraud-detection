"""
Model evaluation metrics and reporting utilities.
"""

import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, classification_report
)

class ModelMetrics:
    """Calculate and report model metrics."""
    
    @staticmethod
    def calculate_all_metrics(y_true, y_pred, y_pred_proba=None):
        """
        Calculate all evaluation metrics.
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
            y_pred_proba: Prediction probabilities
        
        Returns:
            Dictionary with all metrics
        """
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred),
            'recall': recall_score(y_true, y_pred),
            'f1': f1_score(y_true, y_pred),
            'confusion_matrix': confusion_matrix(y_true, y_pred).tolist(),
            'classification_report': classification_report(y_true, y_pred)
        }
        
        if y_pred_proba is not None:
            metrics['roc_auc'] = roc_auc_score(y_true, y_pred_proba)
        
        return metrics
    
    @staticmethod
    def generate_report(metrics):
        """Generate formatted metrics report."""
        report = """
╔════════════════════════════════════════════╗
║          MODEL EVALUATION REPORT           ║
╚════════════════════════════════════════════╝

Accuracy:  {accuracy:.2%}
Precision: {precision:.2%}
Recall:    {recall:.2%}
F1 Score:  {f1:.4f}
ROC-AUC:   {roc_auc:.4f}

Confusion Matrix:
{cm}

Classification Report:
{report}
""".format(
            accuracy=metrics['accuracy'],
            precision=metrics['precision'],
            recall=metrics['recall'],
            f1=metrics['f1'],
            roc_auc=metrics.get('roc_auc', 0),
            cm=metrics['confusion_matrix'],
            report=metrics['classification_report']
        )
        return report
    
    @staticmethod
    def compare_models(models_metrics):
        """Compare metrics across multiple models."""
        comparison = "\nModel Comparison:\n"
        comparison += "=" * 50 + "\n"
        comparison += f"{'Model':<20} {'Accuracy':<15} {'F1 Score':<15}\n"
        comparison += "-" * 50 + "\n"
        
        for model_name, metrics in models_metrics.items():
            comparison += f"{model_name:<20} {metrics['accuracy']:<15.4f} {metrics['f1']:<15.4f}\n"
        
        return comparison
