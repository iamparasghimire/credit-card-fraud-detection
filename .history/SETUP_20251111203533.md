# Configuration and Environment Setup Guide

## Quick Start Commands

### Setup Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

**Option 1: Streamlit GUI (Recommended)**
```bash
streamlit run app.py
```
Opens at: http://localhost:8501

**Option 2: Flask API**
```bash
python api.py
```
API runs at: http://localhost:5000

## File Descriptions

### Core Modules
- **`data_loader.py`**: Data loading, preprocessing, and feature scaling
- **`model_trainer.py`**: ML model training, evaluation, and predictions
- **`app.py`**: Streamlit web dashboard for interactive use
- **`api.py`**: Flask REST API for programmatic access

### Data Files
- **`creditcard.csv`**: Dataset (download from Kaggle)
- **`models/best_fraud_model.pkl`**: Saved trained model (auto-created)

## API Endpoints Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Check API status |
| `/api/train` | POST | Train all models |
| `/api/predict` | POST | Make predictions |
| `/api/data-stats` | POST | Get dataset statistics |
| `/api/model-info` | GET | Get trained model info |

## Environment Variables

Optional environment setup:
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
export STREAMLIT_SERVER_PORT=8501
```

## Troubleshooting

**Can't import modules?**
```bash
pip install -r requirements.txt --upgrade
```

**Port conflicts?**
```bash
streamlit run app.py --server.port 8502
python api.py --port 5001
```

**Out of memory?**
Reduce dataset size or use undersampling in preprocessing.
