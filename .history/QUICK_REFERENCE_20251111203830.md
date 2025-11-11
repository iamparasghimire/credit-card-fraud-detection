# ⚡ Quick Reference Guide

## 🚀 Quick Commands

```bash
# Setup (First time only)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run GUI (Recommended)
streamlit run app.py

# Run API
python api.py

# Run Quick Start
python quickstart.py

# Batch Predictions
python batch_predict.py --input data.csv --output results.csv

# With Docker
docker-compose up
```

## 📊 File Quick Reference

| File | Use Case | Command |
|------|----------|---------|
| `app.py` | Interactive GUI | `streamlit run app.py` |
| `api.py` | REST API | `python api.py` |
| `quickstart.py` | Auto-train | `python quickstart.py` |
| `batch_predict.py` | Bulk predictions | `python batch_predict.py --input in.csv --output out.csv` |
| `data_loader.py` | Data utilities | Import in your code |
| `model_trainer.py` | ML training | Import in your code |

## 🎯 Feature Matrix

| Feature | GUI | API | CLI |
|---------|-----|-----|-----|
| Upload Data | ✅ | ❌ | ❌ |
| Explore Data | ✅ | ✅ | ❌ |
| Train Models | ✅ | ✅ | ✅ |
| Single Predict | ✅ | ✅ | ❌ |
| Batch Predict | ✅ | ✅ | ✅ |
| View Metrics | ✅ | ❌ | ❌ |
| Save Model | ✅ | ✅ | ✅ |

## 📈 Expected Performance

```
Accuracy:   ████████████████████░░░░░░░░░░░░ 95-98%
Precision:  ██████████████░░░░░░░░░░░░░░░░░░ 90-95%
Recall:     █████████████░░░░░░░░░░░░░░░░░░░ 85-95%
F1 Score:   ████████████████░░░░░░░░░░░░░░░░ 0.90-0.95
ROC-AUC:    ██████████████████░░░░░░░░░░░░░░ 0.95-0.99
```

## 🤖 Model Performance Ranking

```
1. Random Forest        ⭐⭐⭐⭐⭐ (Best)
2. SVM                  ⭐⭐⭐⭐
3. KNN                  ⭐⭐⭐⭐
4. Decision Tree        ⭐⭐⭐
5. Logistic Regression  ⭐⭐⭐
6. Naive Bayes          ⭐⭐
```

## 💻 System Requirements

```
CPU: 2+ cores
RAM: 4GB+ (8GB recommended)
Disk: 1GB (for models & data)
Python: 3.8+
OS: Windows, macOS, Linux
```

## 🔑 Key Metrics Explained

```
Accuracy    = (TP + TN) / Total
              → Overall correctness

Precision   = TP / (TP + FP)
              → When we predict fraud, how often correct?

Recall      = TP / (TP + FN)
              → Of actual frauds, how many did we catch?

F1 Score    = 2 * (Precision * Recall) / (Precision + Recall)
              → Balance between precision & recall

ROC-AUC     = Area under ROC curve (0-1)
              → Model discrimination ability
```

## 📊 Confusion Matrix Guide

```
                Predicted
              Normal  |  Fraud
        ───────────────────────
A     Normal   TN    |   FP
c           ────────────────
t     Fraud    FN    |   TP
u   ───────────────────────
a
l

TN = True Negatives  (Correct normal)
FP = False Positives (Normal marked fraud)
FN = False Negatives (Fraud marked normal) ← WORST
TP = True Positives  (Correct fraud)
```

## 🎨 Streamlit GUI Walkthrough

```
HOME PAGE
├─ Welcome message
├─ Feature overview
└─ Upload dataset
    ↓
DATA ANALYSIS
├─ View statistics
├─ Class distribution
├─ Amount analysis
└─ Correlation heatmap
    ↓
MODEL TRAINING
├─ Configure options
├─ Click "Train All Models"
└─ View results table
    ↓
MAKE PREDICTIONS
├─ Single transaction: Enter features manually
└─ Batch: Upload CSV file
    ↓
MODEL PERFORMANCE
├─ View metrics
├─ Confusion matrix
└─ Classification report
```

## 🔌 API Usage Examples

### Health Check
```bash
curl http://localhost:5000/api/health
```

### Train Model
```bash
curl -X POST http://localhost:5000/api/train \
  -H "Content-Type: application/json" \
  -d '{"data_path": "creditcard.csv"}'
```

### Single Prediction
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"transaction": [0.1, -0.2, 0.5, ..., 100.0]}'
```

### Batch Prediction
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"transactions": [[0.1, -0.2, ...], [0.3, 0.1, ...]]}'
```

## 📱 Python API Usage

```python
from data_loader import load_data, preprocess_data
from model_trainer import ModelTrainer

# Load data
data = load_data('creditcard.csv')

# Preprocess
X_train, X_test, y_train, y_test, scaler = preprocess_data(data)

# Train
trainer = ModelTrainer()
trainer.train_all_models(X_train, y_train)

# Evaluate
metrics = trainer.evaluate_best_model(X_test, y_test)
print(f"Accuracy: {metrics['accuracy']}")

# Predict
new_data = [[...features...]]
predictions, probs = trainer.predict(scaler.transform(new_data))

# Save
trainer.save_best_model('my_model.pkl')
```

## 🐛 Troubleshooting Quick Fix

| Problem | Solution |
|---------|----------|
| "No module" | `pip install -r requirements.txt` |
| "File not found" | Download dataset from Kaggle |
| "Port in use" | Change port: `streamlit run app.py --server.port 8502` |
| "Out of memory" | Use undersampling (enabled by default) |
| "All normal" | Check fraud probability scores |
| "Slow training" | Reduce CV folds or dataset size |

## 📚 Documentation Map

```
START HERE
    ↓
GETTING_STARTED.md (Quick start)
    ↓
README.md (Full documentation)
    ↓
PROJECT_SUMMARY.md (What's included)
    ↓
ARCHITECTURE.md (How it works)
    ↓
SETUP.md (Configuration)
    ↓
In-code comments (Implementation details)
```

## 🎓 Learning Path

```
Level 1: Beginner
├─ Read: GETTING_STARTED.md
├─ Run: streamlit run app.py
└─ Try: Upload data & explore

Level 2: Intermediate
├─ Read: README.md
├─ Run: python api.py
└─ Try: API calls with curl/Postman

Level 3: Advanced
├─ Read: ARCHITECTURE.md
├─ Modify: Python source files
└─ Deploy: Docker or production server

Level 4: Expert
├─ Customize: Add new models
├─ Optimize: Hyperparameter tuning
└─ Scale: Cloud deployment
```

## ⏱️ Time Estimates

```
Setup:              5 minutes
Training:           3-5 minutes
First Prediction:   < 1 second
Batch (10k rows):   30 seconds
```

## 🎯 Common Goals & How To

### Goal: Check if transaction is fraud
```
1. streamlit run app.py
2. Go to "Make Predictions"
3. Enter transaction details
4. See fraud probability
```

### Goal: Analyze my dataset
```
1. streamlit run app.py
2. Upload CSV on Home page
3. Go to "Data Analysis"
4. Explore visualizations
```

### Goal: Train custom model
```
1. Edit model_trainer.py
2. Add new model to self.models
3. Run streamlit run app.py
4. Train all models
```

### Goal: Use in my application
```
1. python api.py
2. Make HTTP POST requests
3. Get JSON predictions
```

## 📦 Dependencies at a Glance

```
scikit-learn    → ML algorithms
pandas          → Data handling
numpy           → Numerical operations
matplotlib      → Visualizations
seaborn         → Statistical plots
streamlit       → Web GUI
flask           → REST API
joblib          → Model saving
```

## 🏆 Best Practices

✅ Always download latest dataset from Kaggle
✅ Use undersampling for imbalanced data
✅ Validate on separate test set
✅ Save trained models
✅ Monitor multiple metrics (not just accuracy)
✅ Check confusion matrix for false negatives
✅ Use API for production deployment

## 🚫 Common Mistakes

❌ Using test data for training
❌ Ignoring class imbalance
❌ Only looking at accuracy
❌ Not saving models
❌ Skipping preprocessing
❌ Using same data for train & test

---

**Ready? Start with:**
```bash
streamlit run app.py
```

📖 For more details, see README.md
