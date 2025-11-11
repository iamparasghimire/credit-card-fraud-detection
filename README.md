# 🚨 Credit Card Fraud Detection

ML application to detect fraudulent credit card transactions using Streamlit & Flask.

## � Quick Start

### 1. Install
```bash
pip install -r requirements.txt
```

### 2. Download Dataset
Get `creditcard.csv` from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

### 3. Run
```bash
streamlit run app.py
```
Opens at `http://localhost:8501`

## ✨ Features

- **🎨 Web Dashboard** - Upload data, train models, make predictions
- **🔌 REST API** - `python api.py` at `http://localhost:5000`
- **🤖 6 ML Models** - Random Forest, SVM, KNN, Decision Tree, Logistic Regression, Naive Bayes
- **📊 Analysis** - Fraud patterns, visualizations
- **🔍 Predictions** - Single & batch CSV predictions
- **📈 Performance** - 95-98% Accuracy

## 📁 Files

```
app.py              # Streamlit web dashboard
api.py              # Flask REST API
data_loader.py      # Data preprocessing
model_trainer.py    # ML model training
quickstart.py       # Auto-train script
batch_predict.py    # Batch predictions
requirements.txt    # Dependencies
```

## 📊 Performance

```
Accuracy:  95-98%
Precision: 90-95%
Recall:    85-95%
F1 Score:  0.90-0.95
ROC-AUC:   0.95-0.99
```

## 🐳 Docker

```bash
docker-compose up
```

## ❓ FAQ

**Q: My own dataset?**
A: CSV with 'Class' column (0/1) and 30 features

**Q: Accurate?**
A: ~95-98% on Kaggle dataset

**Q: Deploy?**
A: Use Flask API + Docker

**Q: Error?**
A: Run: `pip install -r requirements.txt --upgrade`

## 📦 Dataset

[Kaggle Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- 284,807 transactions
- 492 frauds (0.17%)

## ‍💻 Author

Paras Ghimire - [@iamparasghimire](https://github.com/iamparasghimire)

## � More Info

See: START_HERE.txt, GETTING_STARTED.md, QUICK_REFERENCE.md

---

**Run:** `streamlit run app.py` 

Made with ❤️
