# 🚨 Credit Card Fraud Detection

A simple and easy-to-use machine learning application to detect fraudulent credit card transactions. Build with Python, Streamlit, and Flask.

## 📋 Quick Start (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Dataset
Download from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and place `creditcard.csv` in project root.

### 3. Run the App
```bash
# For Web Dashboard
streamlit run app.py

# For REST API
python api.py

# For Quick Training
python quickstart.py
```

## ✨ Features

- **🎨 Web Dashboard** - Beautiful Streamlit interface for data exploration and predictions
- **🔌 REST API** - Flask API for integration with other applications
- **🤖 6 ML Models** - Logistic Regression, SVM, Decision Tree, Random Forest, Naive Bayes, KNN
- **📊 Data Analysis** - Visualizations and fraud pattern analysis
- **🔍 Predictions** - Single transaction or batch CSV predictions
- **📈 Metrics** - Accuracy, Precision, Recall, F1, ROC-AUC scores

## 🖥️ Usage

### Web GUI (Easiest)
```bash
streamlit run app.py
# Opens at http://localhost:8501
```

**Features:**
- Upload CSV dataset
- Analyze fraud patterns
- Train models with one click
- Make predictions
- View performance metrics

### REST API
```bash
python api.py
# API runs at http://localhost:5000
```

**Endpoints:**
- `GET /api/health` - Check status
- `POST /api/train` - Train models
- `POST /api/predict` - Make predictions
- `POST /api/data-stats` - Get statistics
- `GET /api/model-info` - Model information

### Command Line
```bash
# Quick start (auto-train all models)
python quickstart.py

# Batch predictions
python batch_predict.py --input data.csv --output results.csv
```

## 📁 Project Files

```
├── app.py                 # Streamlit web dashboard
├── api.py                 # Flask REST API
├── data_loader.py         # Data utilities
├── model_trainer.py       # ML training
├── quickstart.py          # Auto-train script
├── batch_predict.py       # Batch predictions
├── requirements.txt       # Dependencies
├── Dockerfile            # Docker setup
└── docker-compose.yml    # Multi-container setup
```

## 🎯 ML Models

| Model | Accuracy | Status |
|-------|----------|--------|
| Random Forest | ⭐⭐⭐⭐⭐ | Best |
| SVM | ⭐⭐⭐⭐ | Good |
| KNN | ⭐⭐⭐⭐ | Good |
| Decision Tree | ⭐⭐⭐ | Fair |
| Logistic Regression | ⭐⭐⭐ | Fair |
| Naive Bayes | ⭐⭐ | OK |

## 📊 Expected Performance

```
Accuracy:  95-98% ████████████████████░░░░░░░░░░░░
Precision: 90-95% ██████████████░░░░░░░░░░░░░░░░░░
Recall:    85-95% █████████████░░░░░░░░░░░░░░░░░░░
F1 Score:  0.90-0.95 ████████████████░░░░░░░░░░░░░░░░
ROC-AUC:   0.95-0.99 ██████████████████░░░░░░░░░░░░░░
```

## 🐳 Docker

Run everything in Docker:
```bash
docker-compose up
# GUI: http://localhost:8501
# API: http://localhost:5000
```

## 🔧 Dependencies

- Python 3.8+
- scikit-learn (ML algorithms)
- pandas (Data handling)
- numpy (Math operations)
- streamlit (Web GUI)
- flask (REST API)
- matplotlib, seaborn (Visualizations)

See `requirements.txt` for exact versions.

## 📖 Documentation

- **START_HERE.txt** - Visual quick start
- **GETTING_STARTED.md** - Detailed setup guide
- **QUICK_REFERENCE.md** - Commands reference
- **ARCHITECTURE.md** - System design
- **INDEX.md** - Complete navigation guide

## ❓ FAQ

**Q: How do I use this?**
A: Run `streamlit run app.py` and upload your dataset.

**Q: Can I use my own dataset?**
A: Yes! Any CSV with a 'Class' column (0/1) and 30 features will work.

**Q: How accurate is it?**
A: ~95-98% accuracy on the Kaggle dataset.

**Q: Can I deploy to production?**
A: Yes! Use the Flask API with Docker or a cloud platform.

**Q: What if I get an error?**
A: Check QUICK_REFERENCE.md for common solutions.

## 🐛 Troubleshooting

```bash
# Module not found
pip install -r requirements.txt --upgrade

# Port in use
streamlit run app.py --server.port 8502

# Out of memory
# Use undersampling (default) or reduce dataset size
```

## 📦 Dataset

Download from: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

- 284,807 transactions
- 492 frauds (0.17%)
- 30 PCA features + Amount + Time

## 📄 License

MIT License - Feel free to use this project!

## 👨‍💻 Author

**Paras Ghimire**
- GitHub: [@iamparasghimire](https://github.com/iamparasghimire)

## 🙏 Credits

- Dataset: [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Built with: [scikit-learn](https://scikit-learn.org/), [Streamlit](https://streamlit.io/), [Flask](https://flask.palletsprojects.com/)

---

**Get Started:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

Made with ❤️ for fraud detection
