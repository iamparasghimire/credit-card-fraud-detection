"""
Streamlit GUI for credit card fraud detection.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data, preprocess_data, analyze_data
from model_trainer import ModelTrainer
import os

# Page config
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🚨 Credit Card Fraud Detection System")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Select Page",
        ["Home", "Data Analysis", "Model Training", "Make Predictions", "Model Performance"]
    )


# Initialize session state
if 'trainer' not in st.session_state:
    st.session_state.trainer = ModelTrainer()
if 'data' not in st.session_state:
    st.session_state.data = None
if 'scaler' not in st.session_state:
    st.session_state.scaler = None
if 'X_test' not in st.session_state:
    st.session_state.X_test = None
if 'y_test' not in st.session_state:
    st.session_state.y_test = None


# HOME PAGE
if page == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Welcome to Fraud Detection System")
        st.markdown("""
        ### About This Application
        This application uses Machine Learning to detect fraudulent credit card transactions.
        
        #### Features:
        - 📊 **Data Analysis**: Explore transaction patterns and fraud distribution
        - 🤖 **Model Training**: Train multiple ML models and compare performance
        - 🔍 **Predictions**: Detect fraud in single or batch transactions
        - 📈 **Performance Metrics**: View detailed model evaluation results
        
        #### How to Use:
        1. Start by uploading your credit card dataset
        2. Analyze the data distribution
        3. Train the fraud detection model
        4. Use the model to predict fraudulent transactions
        
        #### Dataset Requirements:
        - CSV file with credit card transaction data
        - Must have a 'Class' column (0 = Normal, 1 = Fraud)
        - 30 features expected (V1-V28, Amount, Time)
        """)
    
    with col2:
        st.markdown("""
        ### Quick Stats
        - **Models**: 6 different algorithms
        - **Evaluation**: Cross-validation & test metrics
        - **Metrics**: Accuracy, Precision, Recall, F1, ROC-AUC
        """)
    
    st.markdown("---")
    
    # File uploader
    st.subheader("📁 Upload Dataset")
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        st.session_state.data = pd.read_csv(uploaded_file)
        st.success(f"✅ Dataset loaded! Shape: {st.session_state.data.shape}")
        
        with st.expander("Preview Data"):
            st.dataframe(st.session_state.data.head())


# DATA ANALYSIS PAGE
elif page == "Data Analysis":
    st.header("📊 Data Analysis")
    
    if st.session_state.data is None:
        st.warning("⚠️ Please upload a dataset first from the Home page.")
    else:
        data = st.session_state.data
        
        # Basic statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Transactions", f"{len(data):,}")
        with col2:
            st.metric("Total Features", data.shape[1])
        with col3:
            st.metric("Missing Values", data.isnull().sum().sum())
        with col4:
            fraud_count = (data['Class'] == 1).sum()
            st.metric("Fraudulent Transactions", f"{fraud_count:,}")
        
        st.markdown("---")
        
        # Data analysis
        stats = analyze_data(data)
        
        # Class distribution
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Class Distribution")
            class_data = data['Class'].value_counts()
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(['Normal', 'Fraud'], [class_data[0], class_data[1]], color=['green', 'red'])
            ax.set_ylabel('Count')
            ax.set_title('Transaction Distribution')
            st.pyplot(fig)
        
        with col2:
            st.subheader("Class Percentages")
            fig, ax = plt.subplots(figsize=(8, 4))
            sizes = [stats['normal_percentage'], stats['fraud_percentage']]
            colors = ['green', 'red']
            ax.pie(sizes, labels=['Normal', 'Fraud'], autopct='%1.2f%%', colors=colors, startangle=90)
            ax.set_title('Fraud vs Normal Transactions')
            st.pyplot(fig)
        
        st.markdown("---")
        
        # Amount analysis
        st.subheader("💰 Transaction Amount Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
            fraud_amounts = data[data['Class'] == 1]['Amount']
            normal_amounts = data[data['Class'] == 0]['Amount']
            
            ax1.hist(fraud_amounts, bins=50, color='red', alpha=0.7)
            ax1.set_title('Fraud Transaction Amounts')
            ax1.set_ylabel('Frequency')
            
            ax2.hist(normal_amounts, bins=50, color='green', alpha=0.7)
            ax2.set_title('Normal Transaction Amounts')
            ax2.set_ylabel('Frequency')
            ax2.set_xlabel('Amount ($)')
            
            st.pyplot(fig)
        
        with col2:
            st.markdown("### Amount Statistics")
            amount_stats = stats['amount_stats']
            st.metric("Min Amount", f"${amount_stats['min']:.2f}")
            st.metric("Max Amount", f"${amount_stats['max']:.2f}")
            st.metric("Mean Amount", f"${amount_stats['mean']:.2f}")
            st.metric("Median Amount", f"${amount_stats['median']:.2f}")
        
        st.markdown("---")
        
        # Correlation heatmap
        st.subheader("🔗 Feature Correlation")
        with st.expander("View Correlation Matrix (May be slow for large datasets)"):
            fig, ax = plt.subplots(figsize=(16, 12))
            sns.heatmap(data.corr(), cmap="RdYlGn", ax=ax, cbar_kws={'label': 'Correlation'})
            st.pyplot(fig)


# MODEL TRAINING PAGE
elif page == "Model Training":
    st.header("🤖 Model Training")
    
    if st.session_state.data is None:
        st.warning("⚠️ Please upload a dataset first from the Home page.")
    else:
        st.subheader("Training Configuration")
        
        col1, col2 = st.columns(2)
        with col1:
            test_size = st.slider("Test Set Size", 0.1, 0.5, 0.2)
        with col2:
            cv_folds = st.slider("Cross-Validation Folds", 3, 10, 5)
        
        use_undersampling = st.checkbox("Use Undersampling for Imbalanced Data", value=True)
        
        if st.button("🚀 Train All Models", key="train_button"):
            with st.spinner("Training models... This may take a few minutes."):
                try:
                    data = st.session_state.data
                    
                    # Preprocess data
                    X_train, X_test, y_train, y_test, scaler = preprocess_data(
                        data, 
                        test_size=test_size, 
                        use_undersampling=use_undersampling
                    )
                    
                    # Store in session
                    st.session_state.scaler = scaler
                    st.session_state.X_test = X_test
                    st.session_state.y_test = y_test
                    
                    # Train models
                    results = st.session_state.trainer.train_all_models(X_train, y_train, cv=cv_folds)
                    
                    # Save model
                    os.makedirs('models', exist_ok=True)
                    st.session_state.trainer.save_best_model('models/best_fraud_model.pkl')
                    
                    st.success("✅ Training completed!")
                    
                    # Display results
                    st.subheader("Model Comparison")
                    st.dataframe(results, use_container_width=True)
                    
                    # Highlight best model
                    best_model_row = results.iloc[0]
                    st.info(f"🏆 Best Model: **{best_model_row['model']}** with score: **{best_model_row['best_score']:.4f}**")
                    
                except Exception as e:
                    st.error(f"❌ Error during training: {str(e)}")


# MAKE PREDICTIONS PAGE
elif page == "Make Predictions":
    st.header("🔍 Make Predictions")
    
    if st.session_state.trainer.best_model is None:
        st.warning("⚠️ Please train a model first from the Model Training page.")
    else:
        st.markdown("### Predict Fraud Detection")
        
        pred_type = st.radio("Select Prediction Type", ["Single Transaction", "Batch Transactions"])
        
        if pred_type == "Single Transaction":
            st.subheader("Enter Transaction Features")
            
            col1, col2 = st.columns(2)
            
            with col1:
                amount = st.number_input("Amount ($)", min_value=0.0, value=100.0)
                time = st.number_input("Time", min_value=0.0, value=0.0)
            
            st.markdown("### V Features (V1-V28)")
            
            features = [amount] + [0.0] * 28  # V1-V28
            features.append(time)
            
            # Create sliders for V features
            cols = st.columns(4)
            for i in range(28):
                with cols[i % 4]:
                    features[i + 1] = st.slider(f"V{i+1}", -5.0, 5.0, 0.0, key=f"v{i+1}")
            
            if st.button("🔮 Predict", key="single_predict"):
                try:
                    # Reshape and standardize
                    X = np.array([features])
                    if st.session_state.scaler:
                        X = st.session_state.scaler.transform(X)
                    
                    # Make prediction
                    predictions, probabilities = st.session_state.trainer.predict(X)
                    
                    is_fraud = predictions[0]
                    fraud_prob = probabilities[0][1] if probabilities is not None else 0
                    
                    # Display result
                    col1, col2 = st.columns(2)
                    with col1:
                        if is_fraud:
                            st.error(f"🚨 FRAUD DETECTED! Confidence: {fraud_prob*100:.2f}%")
                        else:
                            st.success(f"✅ Normal Transaction. Fraud Probability: {fraud_prob*100:.2f}%")
                    
                    with col2:
                        fig, ax = plt.subplots(figsize=(6, 4))
                        categories = ['Normal', 'Fraud']
                        probs = [1 - fraud_prob, fraud_prob]
                        colors = ['green', 'red']
                        ax.bar(categories, probs, color=colors)
                        ax.set_ylabel('Probability')
                        ax.set_ylim([0, 1])
                        st.pyplot(fig)
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        else:  # Batch predictions
            st.subheader("Upload Batch Transactions")
            uploaded_file = st.file_uploader("Choose a CSV file with transactions", type=['csv'], key="batch_upload")
            
            if uploaded_file is not None:
                batch_data = pd.read_csv(uploaded_file)
                st.write(f"Loaded {len(batch_data)} transactions")
                
                if st.button("🔮 Predict Batch", key="batch_predict"):
                    try:
                        # Prepare features
                        X = batch_data.drop(columns=['Class'], errors='ignore').values
                        
                        if st.session_state.scaler:
                            X = st.session_state.scaler.transform(X)
                        
                        # Make predictions
                        predictions, probabilities = st.session_state.trainer.predict(X)
                        
                        # Create results dataframe
                        results_df = pd.DataFrame({
                            'Prediction': ['Fraud' if p else 'Normal' for p in predictions],
                            'Fraud_Probability': [probs[1] for probs in probabilities] if probabilities is not None else [0] * len(predictions)
                        })
                        
                        st.subheader("Prediction Results")
                        st.dataframe(results_df, use_container_width=True)
                        
                        # Statistics
                        fraud_count = (predictions == 1).sum()
                        st.metric("Frauds Detected", fraud_count)
                        st.metric("Normal Transactions", len(predictions) - fraud_count)
                        
                        # Download results
                        csv = results_df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Results",
                            data=csv,
                            file_name="fraud_predictions.csv",
                            mime="text/csv"
                        )
                    
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")


# MODEL PERFORMANCE PAGE
elif page == "Model Performance":
    st.header("📈 Model Performance")
    
    if st.session_state.trainer.best_model is None or st.session_state.X_test is None:
        st.warning("⚠️ Please train a model first from the Model Training page.")
    else:
        try:
            X_test = st.session_state.X_test
            y_test = st.session_state.y_test
            
            # Evaluate
            metrics = st.session_state.trainer.evaluate_best_model(X_test, y_test)
            
            st.subheader(f"🏆 Best Model: {metrics['model_name'].replace('_', ' ').title()}")
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Accuracy", f"{metrics['accuracy']*100:.2f}%")
            with col2:
                st.metric("Precision", f"{metrics['precision']*100:.2f}%")
            with col3:
                st.metric("Recall", f"{metrics['recall']*100:.2f}%")
            with col4:
                st.metric("F1 Score", f"{metrics['f1']:.4f}")
            
            if 'roc_auc' in metrics:
                st.metric("ROC-AUC", f"{metrics['roc_auc']:.4f}")
            
            st.markdown("---")
            
            # Confusion Matrix
            st.subheader("Confusion Matrix")
            cm = np.array(metrics['confusion_matrix'])
            
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       xticklabels=['Normal', 'Fraud'],
                       yticklabels=['Normal', 'Fraud'],
                       ax=ax, cbar=False)
            ax.set_xlabel('Predicted')
            ax.set_ylabel('Actual')
            st.pyplot(fig)
            
            st.markdown("---")
            
            # Classification Report
            st.subheader("Classification Report")
            st.text(metrics['classification_report'])
        
        except Exception as e:
            st.error(f"❌ Error evaluating model: {str(e)}")
