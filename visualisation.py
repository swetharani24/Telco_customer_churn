import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from log_file import setup_logging

logger = setup_logging("visualisation")

# =========================
# Plot directory
# =========================
PLOT_DIR = "outputs/plots"
os.makedirs(PLOT_DIR, exist_ok=True)

# =========================
# Save plot helper
# =========================
def save_plot(filename):
    try:
        path = os.path.join(PLOT_DIR, filename)
        plt.tight_layout()
        plt.savefig(path)
        plt.close()
        logger.info(f"Plot saved successfully: {path}")
    except Exception as e:
        logger.error(f"Error saving plot {filename}: {e}")

# =========================
# Load dataset
# =========================
def load_data(path):
    try:
        df = pd.read_csv(path)
        logger.info(f"Dataset loaded: {path} | Shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error loading dataset: {e}")
        return None

# =========================
# Add SIM Operator column
# =========================
def add_sim_operator_column(df, seed=42):
    try:
        np.random.seed(seed)
        operators = ['Airtel', 'BSNL', 'Vodafone', 'Jio']
        probabilities = [0.30, 0.10, 0.20, 0.40]
        df['SIM_Operator'] = np.random.choice(
            operators, size=len(df), p=probabilities
        )
        logger.info("SIM_Operator column added successfully")
        return df
    except Exception as e:
        logger.error(f"Error adding SIM_Operator column: {e}")
        return df

# =========================
# Save dataset
# =========================
def save_dataset(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        logger.info(f"Dataset saved successfully at {output_path}")
    except Exception as e:
        logger.error(f"Error saving dataset: {e}")

# =========================
# Generic bar plot
# =========================
def bar_plot(x, y, xlabel, ylabel, title, filename, figsize=(5,4)):
    try:
        plt.figure(figsize=figsize)
        plt.bar(x, y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        for i, v in enumerate(y):
            plt.text(i, v, str(v), ha='center', va='bottom')
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error creating bar plot {title}: {e}")

# =========================
# Plot functions
# =========================

def plot_churn_distribution(df):
    try:
        churn_counts = df['Churn'].value_counts()
        logger.info(f"Churn distribution:\n{churn_counts}")
        bar_plot(
            churn_counts.index,
            churn_counts.values,
            "Churn",
            "Number of Customers",
            "Churn Distribution",
            "churn_distribution.png"
        )
    except Exception as e:
        logger.error(f"Error in plot_churn_distribution: {e}")

def plot_gender_distribution(df):
    try:
        gender_counts = df['gender'].value_counts()
        logger.info(f"Gender distribution:\n{gender_counts}")
        bar_plot(
            gender_counts.index,
            gender_counts.values,
            "Gender",
            "Number of Customers",
            "Gender Distribution",
            "gender_distribution.png"
        )
    except Exception as e:
        logger.error(f"Error in plot_gender_distribution: {e}")

def plot_tenure_vs_churn(df, filename="tenure_vs_churn.png"):
    try:
        df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
        bins = [0, 18, 36, 54, 72]
        labels = ['Q1 (0–18)', 'Q2 (19–36)', 'Q3 (37–54)', 'Q4 (55–72)']
        df['Tenure_Quarter'] = pd.cut(
            df['tenure'], bins=bins, labels=labels, include_lowest=True
        )
        tenure_churn_q = pd.crosstab(df['Tenure_Quarter'], df['Churn'])
        logger.info(f"Tenure vs Churn:\n{tenure_churn_q}")
        tenure_churn_q.plot(kind='bar', figsize=(6,4))
        plt.xlabel("Tenure Quarter")
        plt.ylabel("Number of Customers")
        plt.title("Tenure Quarter vs Churn")
        plt.xticks(rotation=0)
        plt.legend(title="Churn")
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error in plot_tenure_vs_churn: {e}")

def plot_payment_vs_churn(df, filename="payment_vs_churn.png"):
    try:
        payment_churn = pd.crosstab(df['PaymentMethod'], df['Churn'])
        logger.info(f"Payment vs Churn:\n{payment_churn}")
        payment_churn.plot(kind='bar', figsize=(7,4))
        plt.xlabel("Payment Method")
        plt.ylabel("Number of Customers")
        plt.title("Payment Method vs Churn")
        plt.xticks(rotation=45, ha='right')
        plt.legend(title="Churn")
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error in plot_payment_vs_churn: {e}")

def plot_monthly_charges_quarter(df, filename="monthly_charges_vs_churn.png"):
    try:
        df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
        df['MonthlyCharges_Quarter'] = pd.qcut(
            df['MonthlyCharges'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4']
        )
        quarter_churn = pd.crosstab(df['MonthlyCharges_Quarter'], df['Churn'])
        logger.info(f"Monthly Charges vs Churn:\n{quarter_churn}")
        quarter_churn.plot(kind='bar', figsize=(6,4))
        plt.xlabel("Monthly Charges Quarter")
        plt.ylabel("Number of Customers")
        plt.title("Monthly Charges vs Churn")
        plt.xticks(rotation=0)
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error in plot_monthly_charges_quarter: {e}")

def plot_churn_vs_feature(df, feature, title, filename):
    try:
        churn_feature = pd.crosstab(df[feature], df['Churn'])
        logger.info(f"Churn vs {feature}:\n{churn_feature}")
        churn_feature.plot(kind='bar', figsize=(6,4))
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.title(title)
        plt.xticks(rotation=0)
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error in plot_churn_vs_feature {feature}: {e}")

def plot_gender_vs_internet(df, filename="gender_vs_internet_service.png"):
    try:
        gender_internet = pd.crosstab(df['gender'], df['InternetService'])
        logger.info(f"Gender vs Internet Service:\n{gender_internet}")
        gender_internet.plot(kind='bar', figsize=(7,4))
        plt.xlabel("Gender")
        plt.ylabel("Number of Customers")
        plt.title("Gender vs Internet Service Type")
        plt.xticks(rotation=0)
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error in plot_gender_vs_internet: {e}")

def plot_churn_vs_sim_operator(df, filename="churn_vs_sim_operator.png"):
    try:
        churn_sim = pd.crosstab(df['SIM_Operator'], df['Churn'])
        logger.info(f"Churn vs SIM Operator:\n{churn_sim}")
        ax = churn_sim.plot(kind='bar', figsize=(7,5))
        ax.set_xlabel("SIM Operator")
        ax.set_ylabel("Number of Customers")
        ax.set_title("Churn Distribution by SIM Operator")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
        for container in ax.containers:
            ax.bar_label(container)
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error in plot_churn_vs_sim_operator: {e}")

def plot_simtype_vs_gender(df, filename="sim_operator_vs_gender.png"):
    try:
        df['SIM_Operator'].fillna('Unknown', inplace=True)
        sim_gender_counts = pd.crosstab(df['SIM_Operator'], df['gender'])
        logger.info(f"SIM Operator vs Gender:\n{sim_gender_counts}")
        sim_gender_counts.plot(kind='bar', figsize=(7,5))
        plt.xlabel("SIM Operator")
        plt.ylabel("Number of Customers")
        plt.title("SIM Operator Distribution by Gender")
        plt.xticks(rotation=0)
        plt.legend(title="Gender")
        save_plot(filename)
    except Exception as e:
        logger.error(f"Error in plot_simtype_vs_gender: {e}")

# =========================
# MAIN
# =========================
def main():
    try:
        logger.info("Visualisation module started")

        df = load_data("WA_Fn-UseC_-Telco-Customer-Churn.csv")
        if df is None:
            logger.error("Dataset not found. Exiting.")
            return

        df = add_sim_operator_column(df)
        save_dataset(df, "Telco_Customer_Churn_with_SIM.csv")

        # Call all plots
        plot_churn_distribution(df)
        plot_gender_distribution(df)
        plot_tenure_vs_churn(df)
        plot_payment_vs_churn(df)
        plot_monthly_charges_quarter(df)
        plot_churn_vs_feature(df, 'gender', "Churn by Gender", "churn_vs_gender.png")
        plot_churn_vs_feature(df, 'Contract', "Churn by Contract Type", "churn_vs_contract.png")
        plot_gender_vs_internet(df)
        plot_churn_vs_sim_operator(df)
        plot_simtype_vs_gender(df)

        logger.info("Visualisation module completed successfully")
    except Exception as e:
        logger.error(f"Visualisation pipeline failed: {e}")

if __name__ == "__main__":
    main()
