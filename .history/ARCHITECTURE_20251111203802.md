# 🏗️ Architecture & Components

## 📐 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     FRAUD DETECTION SYSTEM                      │
└─────────────────────────────────────────────────────────────────┘

┌────────────────────┐         ┌────────────────────┐
│  Streamlit GUI     │         │   Flask REST API   │
│  (app.py)          │         │   (api.py)         │
│                    │         │                    │
│ • Data Upload      │         │ • HTTP Endpoints   │
│ • Analysis         │         │ • JSON Response    │
│ • Training         │         │ • CORS Support     │
│ • Predictions      │         │ • Model Management │
│ • Performance      │         │ • Batch Predict    │
└────────┬───────────┘         └────────┬───────────┘
         │                              │
         └──────────────┬───────────────┘
                        │
         ┌──────────────▼──────────────┐
         │   ML Pipeline (Core)        │
         │                             │
         │  ┌───────────────────────┐ │
         │  │  data_loader.py       │ │
         │  │  • Load CSV           │ │
         │  │  • Preprocess         │ │
         │  │  • Scale Features     │ │
         │  │  • Train/Test Split   │ │
         │  └───────────┬───────────┘ │
         │              │             │
         │  ┌───────────▼───────────┐ │
         │  │  model_trainer.py     │ │
         │  │  • 6 ML Models        │ │
         │  │  • GridSearchCV       │ │
         │  │  • Cross Validation   │ │
         │  │  • Evaluation Metrics │ │
         │  │  • Model Persistence  │ │
         │  └───────────┬───────────┘ │
         │              │             │
         │  ┌───────────▼───────────┐ │
         │  │   Predictions         │ │
         │  │  • Single Transaction │ │
         │  │  • Batch Processing   │ │
         │  │  • Confidence Scores  │ │
         │  └───────────────────────┘ │
         │                             │
         └─────────────┬───────────────┘
                       │
         ┌─────────────▼──────────────┐
         │   Model Storage            │
         │   models/                  │
         │   └── best_fraud_model.pkl │
         └────────────────────────────┘
```

## 🔄 Data Flow

```
1. INPUT DATA
   ↓
creditcard.csv (284,807 transactions)
   ↓
2. DATA LOADING & EXPLORATION
   ├─ Load CSV
   ├─ Analyze statistics
   ├─ Check missing values
   └─ Class distribution
   ↓
3. PREPROCESSING
   ├─ Handle imbalance (undersampling)
   ├─ Split train/test (80/20)
   ├─ StandardScaler normalization
   └─ Feature preparation
   ↓
4. MODEL TRAINING
   ├─ Logistic Regression
   ├─ SVM
   ├─ Decision Tree
   ├─ Random Forest (usually best)
   ├─ Naive Bayes
   └─ KNN
   ↓
5. MODEL EVALUATION
   ├─ Cross-validation (5 folds)
   ├─ Calculate metrics
   ├─ Select best model
   └─ Save to disk
   ↓
6. PREDICTIONS
   ├─ Load trained model
   ├─ Scale new data
   ├─ Make predictions
   └─ Return probability scores
   ↓
OUTPUT
   ├─ Fraud/Normal classification
   ├─ Confidence percentage
   └─ Detailed metrics
```

## 📦 Module Dependencies

```
requirements.txt
    │
    ├─► scikit-learn (ML algorithms)
    │       ↓
    │   [Logistic Regression, SVM, Decision Tree,
    │    Random Forest, Naive Bayes, KNN,
    │    GridSearchCV, train_test_split, metrics]
    │
    ├─► pandas (Data manipulation)
    │       ↓
    │   [DataFrame operations, CSV reading]
    │
    ├─► numpy (Numerical operations)
    │       ↓
    │   [Array operations, statistics]
    │
    ├─► matplotlib (Visualization)
    │       ↓
    │   [Plotting, charts]
    │
    ├─► seaborn (Statistical visualization)
    │       ↓
    │   [Heatmaps, advanced plots]
    │
    ├─► streamlit (Web GUI)
    │       ↓
    │   [Web interface, interactive dashboard]
    │
    ├─► flask (REST API)
    │       ↓
    │   [HTTP server, endpoints, JSON]
    │
    ├─► flask-cors (API enhancement)
    │       ↓
    │   [Cross-origin resource sharing]
    │
    └─► joblib (Model persistence)
            ↓
        [Save/load trained models]
```

## 🎯 Component Interaction

```
User/Client
    │
    ├─────────────────┬─────────────────┐
    │                 │                 │
    ▼                 ▼                 ▼
┌─────────────┐ ┌──────────────┐ ┌─────────────┐
│ Streamlit   │ │  Flask API   │ │ Python CLI  │
│ GUI         │ │  REST        │ │ Scripts     │
└──────┬──────┘ └──────┬───────┘ └──────┬──────┘
       │                │               │
       ▼                ▼               ▼
   ┌────────────────────────────────────────┐
   │    Main ML Pipeline                    │
   │                                        │
   │  • data_loader.py                      │
   │    - load_data()                       │
   │    - preprocess_data()                 │
   │    - analyze_data()                    │
   │                                        │
   │  • model_trainer.py                    │
   │    - train_all_models()                │
   │    - evaluate_best_model()             │
   │    - predict()                         │
   │    - save_best_model()                 │
   │    - load_model()                      │
   │                                        │
   └────────────┬──────────────┬────────────┘
                │              │
        ┌───────▼───────┐  ┌────▼─────────┐
        │ Training Data │  │ Test Data    │
        │  X_train      │  │  X_test      │
        │  y_train      │  │  y_test      │
        └───────┬───────┘  └────┬─────────┘
                │               │
                └───────┬───────┘
                        │
        ┌───────────────▼─────────────────┐
        │   Model Evaluation Metrics      │
        │                                 │
        │  • Accuracy: 95-98%             │
        │  • Precision: 90-95%            │
        │  • Recall: 85-95%               │
        │  • F1 Score: 0.90-0.95          │
        │  • ROC-AUC: 0.95-0.99           │
        │  • Confusion Matrix             │
        │                                 │
        └───────────────┬─────────────────┘
                        │
        ┌───────────────▼─────────────────┐
        │   Selected Best Model           │
        │   (Usually Random Forest)       │
        │   Saved to: models/             │
        │             best_fraud_model.pkl│
        └───────────────┬─────────────────┘
                        │
        ┌───────────────▼─────────────────┐
        │   Predictions                   │
        │                                 │
        │  Input: New Transaction         │
        │  Output: [Fraud%: 92%, Normal%] │
        │                                 │
        └─────────────────────────────────┘
```

## 🔌 API Endpoints Map

```
Flask Server (api.py)
│
├─ GET /api/health
│   └─ Check if API is running
│
├─ POST /api/train
│   ├─ Input: {"data_path": "creditcard.csv"}
│   └─ Output: Training results & metrics
│
├─ POST /api/predict
│   ├─ Input (Single): {"transaction": [features]}
│   ├─ Input (Batch): {"transactions": [[f1], [f2]]}
│   └─ Output: {"is_fraud": bool, "probability": float}
│
├─ POST /api/data-stats
│   ├─ Input: {"data_path": "creditcard.csv"}
│   └─ Output: Dataset statistics
│
└─ GET /api/model-info
    ├─ Input: None
    └─ Output: Model name & parameters
```

## 🖥️ Streamlit Pages Map

```
Streamlit App (app.py)
│
├─ HOME 📚
│   ├─ Welcome & Overview
│   ├─ Feature description
│   └─ Dataset uploader
│
├─ DATA ANALYSIS 📊
│   ├─ Basic statistics
│   ├─ Class distribution (bar + pie)
│   ├─ Amount analysis (histograms)
│   ├─ Correlation heatmap
│   └─ Fraud metrics
│
├─ MODEL TRAINING 🤖
│   ├─ Configuration options
│   │   ├─ Test size slider
│   │   ├─ CV folds slider
│   │   └─ Undersampling toggle
│   ├─ Train button
│   └─ Results comparison table
│
├─ MAKE PREDICTIONS 🔍
│   ├─ Single Transaction
│   │   ├─ Feature input sliders
│   │   └─ Real-time prediction
│   └─ Batch Transactions
│       ├─ CSV uploader
│       └─ Bulk predictions
│
└─ MODEL PERFORMANCE 📈
    ├─ Accuracy, Precision, Recall, F1
    ├─ Confusion Matrix
    └─ Classification Report
```

## 📊 ML Model Pipeline

```
Raw Data (284,807 rows × 31 cols)
    │
    ▼
Class Imbalance Analysis
    │ 0.17% fraud (rare)
    │ 99.83% normal (common)
    │
    ▼
Undersampling Strategy
    │
    ├─ Frauds: 492
    └─ Normal: 492 (sampled)
    │
    ▼
Balanced Dataset (984 rows)
    │
    ▼
Train/Test Split (80/20)
    │
    ├─ Train: 787 samples
    └─ Test: 197 samples
    │
    ▼
StandardScaler (Feature Normalization)
    │
    ├─ Mean = 0
    └─ StdDev = 1
    │
    ▼
Model Training (6 algorithms)
    │
    ├─ Algorithm 1: Logistic Regression
    │   └─ GridSearchCV(solver=['liblinear'])
    │
    ├─ Algorithm 2: SVM
    │   └─ GridSearchCV(kernel, C)
    │
    ├─ Algorithm 3: Decision Tree
    │   └─ GridSearchCV(criterion)
    │
    ├─ Algorithm 4: Random Forest
    │   └─ GridSearchCV(criterion, n_estimators)
    │
    ├─ Algorithm 5: Naive Bayes
    │   └─ No hyperparameters
    │
    └─ Algorithm 6: KNN
        └─ GridSearchCV(n_neighbors)
    │
    ▼
Cross-Validation (5-Fold)
    │
    ├─ Fold 1: Train on 4, Validate on 1
    ├─ Fold 2: Train on 4, Validate on 1
    ├─ Fold 3: Train on 4, Validate on 1
    ├─ Fold 4: Train on 4, Validate on 1
    └─ Fold 5: Train on 4, Validate on 1
    │
    ▼
Best Model Selection
    │ (Usually Random Forest)
    │
    ▼
Final Evaluation on Test Set
    │
    ├─ Accuracy: ~95-98%
    ├─ Precision: ~90-95%
    ├─ Recall: ~85-95%
    ├─ F1 Score: ~0.90-0.95
    ├─ ROC-AUC: ~0.95-0.99
    └─ Confusion Matrix
    │
    ▼
Model Saved (joblib)
    │
    ▼
Ready for Production
```

## 🚀 Deployment Architecture

```
Option 1: Local Development
├─ streamlit run app.py
└─ GUI at localhost:8501

Option 2: Docker Container
├─ docker build -t fraud-detector .
├─ docker run -p 8501:8501 fraud-detector
└─ GUI at localhost:8501

Option 3: Docker Compose
├─ docker-compose up
├─ GUI at localhost:8501
└─ API at localhost:5000

Option 4: Production Server
├─ Flask API + Gunicorn
├─ Nginx Reverse Proxy
├─ SSL/TLS Encryption
└─ Load Balancer
```

---

This architecture ensures:
✅ Modularity - Easy to modify
✅ Scalability - Handle large datasets
✅ Production-Ready - Error handling & logging
✅ Flexibility - CLI, API, and GUI options
✅ Maintainability - Well-organized code
