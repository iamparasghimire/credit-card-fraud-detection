"""
Model comparison and performance analysis utilities.
"""

import pandas as pd
from typing import Dict, List

class ModelComparison:
    """Compare and analyze multiple model performances."""
    
    def __init__(self):
        self.comparison_data = []
    
    def add_model_result(self, model_name: str, metrics: Dict):
        """Add a model's performance metrics."""
        self.comparison_data.append({
            'Model': model_name,
            **metrics
        })
    
    def get_dataframe(self) -> pd.DataFrame:
        """Get comparison as DataFrame."""
        return pd.DataFrame(self.comparison_data)
    
    def get_best_model(self, metric: str = 'f1') -> str:
        """Get best model by metric."""
        if not self.comparison_data:
            return None
        df = self.get_dataframe()
        return df.loc[df[metric].idxmax(), 'Model']
    
    def get_ranking(self, metric: str = 'f1') -> List[str]:
        """Get models ranked by metric."""
        if not self.comparison_data:
            return []
        df = self.get_dataframe()
        return df.sort_values(metric, ascending=False)['Model'].tolist()
    
    def get_summary(self) -> str:
        """Generate comparison summary."""
        if not self.comparison_data:
            return "No models to compare."
        
        df = self.get_dataframe()
        summary = "\n" + "="*60 + "\n"
        summary += "MODEL COMPARISON SUMMARY\n"
        summary += "="*60 + "\n"
        summary += df.to_string(index=False) + "\n"
        summary += "="*60 + "\n"
        summary += f"\nBest Model (F1): {self.get_best_model('f1')}\n"
        summary += f"Best Model (Accuracy): {self.get_best_model('accuracy')}\n"
        summary += "="*60 + "\n"
        
        return summary
    
    def get_best_performers(self, top_n: int = 3) -> Dict:
        """Get top N models by different metrics."""
        if not self.comparison_data:
            return {}
        
        df = self.get_dataframe()
        return {
            'top_f1': df.nlargest(top_n, 'f1')[['Model', 'f1']].values.tolist(),
            'top_accuracy': df.nlargest(top_n, 'accuracy')[['Model', 'accuracy']].values.tolist(),
            'top_precision': df.nlargest(top_n, 'precision')[['Model', 'precision']].values.tolist(),
            'top_recall': df.nlargest(top_n, 'recall')[['Model', 'recall']].values.tolist(),
        }
