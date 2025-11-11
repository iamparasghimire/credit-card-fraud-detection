"""
Performance optimization and caching utilities.
"""

import time
import hashlib
import pickle
from functools import wraps
from typing import Any, Callable
import os
from datetime import datetime, timedelta

class PerformanceOptimizer:
    """Optimize model and data processing performance."""
    
    @staticmethod
    def measure_time(func: Callable) -> Callable:
        """Decorator to measure function execution time."""
        @wraps(func)
        def wrapper(*args, **kwargs) -> tuple:
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            return result, elapsed_time
        return wrapper
    
    @staticmethod
    def cache_with_expiry(cache_dir: str = '.cache', expiry_hours: int = 24):
        """Decorator to cache function results with expiry."""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                # Create cache directory if not exists
                os.makedirs(cache_dir, exist_ok=True)
                
                # Generate cache key from function name and arguments
                cache_key = hashlib.md5(
                    f"{func.__name__}_{str(args)}_{str(kwargs)}".encode()
                ).hexdigest()
                cache_file = os.path.join(cache_dir, f"{cache_key}.cache")
                
                # Check if cache exists and is fresh
                if os.path.exists(cache_file):
                    file_time = os.path.getmtime(cache_file)
                    if datetime.now() - datetime.fromtimestamp(file_time) < timedelta(hours=expiry_hours):
                        with open(cache_file, 'rb') as f:
                            return pickle.load(f)
                
                # Execute function and cache result
                result = func(*args, **kwargs)
                with open(cache_file, 'wb') as f:
                    pickle.dump(result, f)
                
                return result
            return wrapper
        return decorator
    
    @staticmethod
    def batch_process(items, batch_size: int, process_func: Callable):
        """Process items in batches for better memory efficiency."""
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            batch_results = process_func(batch)
            results.extend(batch_results)
        return results
    
    @staticmethod
    def profile_memory(func: Callable) -> Callable:
        """Decorator to profile memory usage."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                import psutil
                import os
                process = psutil.Process(os.getpid())
                mem_before = process.memory_info().rss / 1024 / 1024  # MB
                
                result = func(*args, **kwargs)
                
                mem_after = process.memory_info().rss / 1024 / 1024  # MB
                mem_used = mem_after - mem_before
                
                return result, mem_used
            except ImportError:
                return func(*args, **kwargs), None
        return wrapper


class CacheManager:
    """Manage caching for model predictions and data."""
    
    def __init__(self, cache_dir: str = '.cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def clear_old_cache(self, hours: int = 24):
        """Remove cache files older than specified hours."""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        removed_count = 0
        
        for filename in os.listdir(self.cache_dir):
            filepath = os.path.join(self.cache_dir, filename)
            if os.path.isfile(filepath):
                if datetime.fromtimestamp(os.path.getmtime(filepath)) < cutoff_time:
                    os.remove(filepath)
                    removed_count += 1
        
        return removed_count
    
    def get_cache_size(self) -> float:
        """Get total cache size in MB."""
        total_size = 0
        for filename in os.listdir(self.cache_dir):
            filepath = os.path.join(self.cache_dir, filename)
            if os.path.isfile(filepath):
                total_size += os.path.getsize(filepath)
        return total_size / 1024 / 1024
    
    def clear_all_cache(self):
        """Clear all cached files."""
        for filename in os.listdir(self.cache_dir):
            filepath = os.path.join(self.cache_dir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
