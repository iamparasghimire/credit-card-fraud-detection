# 🎯 Getting Started Guide

## 📥 Installation (5 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/iamparasghimire/credit-card-fraud-detection.git
cd credit-card-fraud-detection

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download dataset
# Visit: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
# Download creditcard.csv and place it in the project root
```

## 🚀 Running the Application

### Option A: Interactive Web GUI (Recommended for beginners)
```bash
streamlit run app.py
```
✅ Opens at `http://localhost:8501`

**What you can do:**
- Upload credit card dataset
- Analyze fraud patterns
- Train models with custom parameters
- Make single/batch predictions
- View detailed performance metrics

### Option B: REST API (For developers/integration)
```bash
python api.py
```
✅ API runs at `http://localhost:5000`

**Test the API:**
```bash
# Check health
curl http://localhost:5000/api/health

# Train model
curl -X POST http://localhost:5000/api/train \
  -H "Content-Type: application/json" \
  -d '{"data_path": "creditcard.csv"}'

# Make prediction
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"transaction": [0.1, -0.2, 0.5, ..., 100.0]}'
```

### Option C: Quick Start Script
```bash
python quickstart.py
```
✅ Automatically trains all models and shows results

### Option D: Batch Processing
```bash
python batch_predict.py --input transactions.csv --output predictions.csv
```

## 🐳 Docker (One-command deployment)

```bash
# Build and run both GUI and API
docker-compose up

# GUI: http://localhost:8501
# API: http://localhost:5000
```

## 📊 What Each File Does

| File | Purpose |
|------|---------|
| `app.py` | 🎨 Streamlit web interface |
| `api.py` | 🔌 Flask REST API server |
| `data_loader.py` | 📂 Data loading & preprocessing |
| `model_trainer.py` | 🤖 ML model training & evaluation |
| `batch_predict.py` | 📋 Batch prediction utility |
| `quickstart.py` | ⚡ Quick start script |
| `requirements.txt` | 📦 Python dependencies |
| `Dockerfile` | 🐳 Docker container config |
| `docker-compose.yml` | 🐳 Multi-container setup |

## 🎓 Typical Workflow

### Step 1: Prepare Data
```
Upload creditcard.csv to project root
```

### Step 2: Explore Data
```bash
streamlit run app.py
→ Go to "Data Analysis" page
```

### Step 3: Train Models
```
Click "Train All Models" button in Streamlit
→ Wait for training to complete
→ View model comparison
```

### Step 4: Make Predictions
```
Go to "Make Predictions" page
→ Either single transaction or batch CSV
→ View results with confidence scores
```

### Step 5: Evaluate Performance
```
Go to "Model Performance" page
→ View metrics and confusion matrix
```

## 💡 Quick Tips

### Tip 1: First time setup?
```bash
python quickstart.py  # This does everything automatically
```

### Tip 2: Want to use the API only?
```python
from data_loader import load_data, preprocess_data
from model_trainer import ModelTrainer
import requests

# OR use curl/REST client to call API endpoints
```

### Tip 3: Have a large dataset?
The app handles up to 500MB comfortably. For larger:
- Use undersampling (enabled by default)
- Reduce cross-validation folds
- Use batch prediction on chunks

### Tip 4: Want to integrate with your app?
Use the Flask API (`python api.py`) and make HTTP requests

## 🎯 Model Comparison

Six algorithms are trained automatically:

| Model | Speed | Accuracy | Best For |
|-------|-------|----------|----------|
| Logistic Regression | ⚡⚡⚡ | ⭐⭐⭐ | Baseline |
| SVM | ⚡⚡ | ⭐⭐⭐⭐ | Complex patterns |
| Decision Tree | ⚡⚡⚡ | ⭐⭐⭐ | Interpretability |
| Random Forest | ⚡ | ⭐⭐⭐⭐⭐ | Best overall |
| Naive Bayes | ⚡⚡⚡ | ⭐⭐ | Probabilistic |
| KNN | ⚡⚡ | ⭐⭐⭐⭐ | Local patterns |

## ❓ FAQ

**Q: Why is training slow?**
A: GridSearchCV tests multiple hyperparameters. Reduce CV folds in settings.

**Q: My predictions are all "Normal"?**
A: This is expected - fraud is rare (~0.17%). Check confidence scores and adjust threshold.

**Q: Can I use a different dataset?**
A: Yes! As long as it has a 'Class' column (0/1) and 30 features.

**Q: How do I save my trained model?**
A: It auto-saves to `models/best_fraud_model.pkl`. Use `trainer.load_model()` to reuse.

**Q: Can I deploy this to production?**
A: Yes! Use the Docker setup or API with a production WSGI server like Gunicorn.

## 🔧 Customization

### Train only specific models:
Edit `model_trainer.py` and remove models from `self.models` dict

### Adjust preprocessing:
Edit `preprocess_data()` in `data_loader.py`

### Change API port:
```bash
python api.py --port 5001
```

### Streamlit settings:
Create `.streamlit/config.toml`:
```toml
[server]
port = 8502
runOnSave = true
```

## 📈 Next Steps

After getting familiar:
1. ✅ Try different datasets
2. ✅ Experiment with hyperparameters
3. ✅ Add custom preprocessing
4. ✅ Deploy with Docker
5. ✅ Integrate with your system via API

## 🐛 Troubleshooting

**"Module not found" error:**
```bash
pip install -r requirements.txt --upgrade
```

**"creditcard.csv not found":**
```
Download from https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
Place in project root
```

**Port already in use:**
```bash
# Change port in code or use different one
streamlit run app.py --server.port 8502
```

**Memory issues:**
```bash
# Use undersampling (default) or reduce dataset size
```

## 📞 Support

- 📖 Read README.md for detailed documentation
- 🔧 Check SETUP.md for configuration
- 🐛 Check individual file docstrings
- 💬 Open an issue on GitHub

---

**Ready to detect fraud? Start with:**
```bash
streamlit run app.py
```

🚀 Happy fraud detecting!
