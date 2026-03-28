# Customer Churn Prediction Project

## Project Overview
This project focuses on **predicting customer churn**, helping businesses identify which customers are likely to leave and take proactive measures to retain them. The project is divided into **two phases**:  

---

## Phase 1: Data Cleaning and Exploration
In the first phase, multiple customer datasets were collected, including:
- **Customer Demographics**  
- **Transaction History**  
- **Customer Service Interactions**  
- **Online Activity**
- **Churn Status** 

Key tasks in Phase 1 included:  
- **Merging multiple sheets** into a single dataset for analysis.  
- **Cleaning and preprocessing** data to handle missing values, inconsistent formats, and non-numeric features.  
- **Exploratory data analysis (EDA)** to understand patterns, distributions, and relationships between features and churn.  
- **Visualizations** such as bar charts, histograms, and correlation plots to interpret key factors contributing to churn.

The outcome of Phase 1 was a **cleaned and processed dataset**, ready for modeling.

**Tools and libraries used in Phase 1:**  
- Python  
- pandas (data manipulation)  
- numpy (numerical computations)  
- matplotlib & seaborn (visualizations)  

---

## Phase 2: Predictive Modeling
The second phase involved **building a machine learning model** to predict customer churn. Steps included:  

- **Understanding the problem type**: binary classification for churn prediction.  
- **Feature selection** to identify numeric columns that influence churn.  
- **Data preprocessing**: scaling numerical features, encoding categorical features, and handling imbalanced classes.  
- **Model training**: testing different algorithms and selecting the best performer.  
- **Model evaluation** using metrics like accuracy, ROC-AUC score, and confusion matrices.  
- **Deployment**: creating a **Streamlit web app** for real-time churn predictions.  

**Tools and libraries used in Phase 2:**  
- scikit-learn (machine learning and preprocessing)  
- joblib (saving/loading models)  
- Streamlit (web app development)  
- Python (general programming)  

---

## Files in the Repository
- `app.py` → Streamlit app for interactive predictions  
- `churn_model.pkl` → Trained machine learning model  
- cleaned datasets used during model development  
- certificate of completion
---

## Key Highlights
- Demonstrates the **full data science pipeline**: data cleaning → feature engineering → modeling → deployment.  
- Focuses on **imbalanced dataset handling** and **binary classification**.  
- Shows practical application of **Python, pandas, scikit-learn, and Streamlit** to a real-world business problem.  

---

## Author
Firdausi Jibrin
