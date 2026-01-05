📊 Telco Customer Churn – Exploratory Data Analysis (EDA) & Data Preparation

📌 Project Overview

Customer churn is a major challenge in the telecom industry.
This project focuses on exploratory data analysis (EDA) and data preprocessing to understand customer behavior and prepare the dataset for building a churn prediction machine learning model.

🎯 Objective

Analyze customer churn patterns

Clean and preprocess raw data

Perform visual exploratory analysis

Encode features for machine learning readiness

📂 Dataset Information

Dataset Name: Telco Customer Churn

Source: IBM Sample Dataset

Records: ~7,000 customers

Features: 21

Target Variable: Churn (Yes / No)

🛠️ Tools & Technologies

Python

Pandas

Matplotlib

VS Code

Git & GitHub

🔄 Project Workflow

Data Loading

Data Cleaning

Exploratory Data Analysis (EDA)

Feature Engineering & Encoding

Dataset Preparation for ML

🧹 Data Cleaning Steps

Removed duplicate records

Converted TotalCharges to numeric

Handled missing values using median imputation

Checked categorical consistency

Identified outliers using boxplots (retained as valid data)

📊 Exploratory Data Analysis (EDA)

Key visualizations include:

Churn distribution

Churn vs Contract Type

Churn vs Tenure

Monthly Charges distribution

Gender vs Churn

🔍 Key Insights

Month-to-month contracts show higher churn

Customers with lower tenure are more likely to churn

Higher monthly charges correlate with higher churn

Gender has minimal impact on churn

🔁 Feature Engineering & Encoding

Dropped irrelevant column (customerID)

Binary encoding for Yes/No features

One-hot encoding for multi-category features

Ensured all features are numeric and ML-ready
