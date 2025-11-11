"""
Requirements management and environment setup utilities.
"""

CORE_DEPENDENCIES = {
    'pandas': '>=2.0.0',
    'numpy': '>=1.24.0',
    'scikit-learn': '>=1.3.0'
}

ML_DEPENDENCIES = {
    'matplotlib': '>=3.7.0',
    'seaborn': '>=0.12.0'
}

WEB_DEPENDENCIES = {
    'streamlit': '>=1.27.0',
    'flask': '>=2.3.0',
    'flask-cors': '>=4.0.0'
}

MODEL_DEPENDENCIES = {
    'joblib': '>=1.3.0'
}

DEV_DEPENDENCIES = {
    'pytest': '>=7.0.0',
    'pytest-cov': '>=4.0.0'
}

ALL_DEPENDENCIES = {
    **CORE_DEPENDENCIES,
    **ML_DEPENDENCIES,
    **WEB_DEPENDENCIES,
    **MODEL_DEPENDENCIES,
    **DEV_DEPENDENCIES
}

def get_requirements_list():
    """Get list of all requirements."""
    return [f"{pkg}{version}" for pkg, version in ALL_DEPENDENCIES.items()]

def print_dependencies():
    """Print all dependencies grouped by category."""
    print("Core Dependencies:")
    for pkg, version in CORE_DEPENDENCIES.items():
        print(f"  {pkg}{version}")
    
    print("\nML Dependencies:")
    for pkg, version in ML_DEPENDENCIES.items():
        print(f"  {pkg}{version}")
    
    print("\nWeb Dependencies:")
    for pkg, version in WEB_DEPENDENCIES.items():
        print(f"  {pkg}{version}")
    
    print("\nModel Dependencies:")
    for pkg, version in MODEL_DEPENDENCIES.items():
        print(f"  {pkg}{version}")
    
    print("\nDevelopment Dependencies:")
    for pkg, version in DEV_DEPENDENCIES.items():
        print(f"  {pkg}{version}")
