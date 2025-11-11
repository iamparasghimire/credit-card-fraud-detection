"""
Logging utilities for the fraud detection system.
"""

import logging
import os
from datetime import datetime

def setup_logging(log_file='logs/fraud_detection.log', level=logging.INFO):
    """
    Setup logging configuration for the application.
    
    Args:
        log_file: Path to log file
        level: Logging level
    
    Returns:
        Logger instance
    """
    os.makedirs(os.path.dirname(log_file) if os.path.dirname(log_file) else '.', exist_ok=True)
    
    logger = logging.getLogger('FraudDetection')
    logger.setLevel(level)
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def get_logger(name):
    """Get logger instance."""
    return logging.getLogger(f'FraudDetection.{name}')
