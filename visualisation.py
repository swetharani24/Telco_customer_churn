import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from log_file import setup_logging

logger = setup_logging("visualisation")


# =========================
# Load Dataset
# =========================
def load_data(path):
    df = pd.read_csv(path)
    logger.info(df.head())
    df.info()
    return df

import pandas as pd
import numpy as np

# =========================
# Load Data
# =========================
def load_data(path):
    return pd.read_csv(path)

# =========================
# Add SIM Operator Column
# =========================
def add_sim_operator_column(df, seed=42):
    np.random.seed(seed)

    operators = ['Airtel', 'BSNL', 'Vodafone', 'Jio']
    probabilities = [0.30, 0.10, 0.20, 0.40]

    df['SIM_Operator'] = np.random.choice(
        operators,
        size=len(df),
        p=probabilities
    )
    return df
def save_dataset(df, output_path):
    df.to_csv(output_path, index=False)
    logger.info(f"Dataset saved successfully at {output_path}")




# Bar Plot with Count Labels
# =========================
def bar_plot(x, y, xlabel, ylabel, title, figsize=(5,4)):
    plt.figure(figsize=figsize)
    plt.bar(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    for i, v in enumerate(y):
        plt.text(i, v, str(v), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


# =========================
# Churn Distribution
# =========================
def plot_churn_distribution(df):
    churn_counts = df['Churn'].value_counts()
    bar_plot(
        churn_counts.index,
        churn_counts.values,
        "Churn",
        "Number of Customers",
        "Churn Distribution"
    )


# =========================
# Gender Distribution
# =========================
def plot_gender_distribution(df):
    gender_counts = df['gender'].value_counts()
    bar_plot(
        gender_counts.index,
        gender_counts.values,
        "Gender",
        "Count",
        "Gender Distribution"
    )


# =========================
# Gender vs Senior Citizen
# =========================
def plot_gender_senior(df):
    gender_senior = pd.crosstab(df['SeniorCitizen'], df['gender'])
    gender_senior.index = ['Non-Senior', 'Senior']

    x = np.arange(len(gender_senior.index))
    width = 0.35

    plt.figure(figsize=(6,5))
    bars1 = plt.bar(x - width/2, gender_senior['Female'], width, label='Female')
    bars2 = plt.bar(x + width/2, gender_senior['Male'], width, label='Male')

    plt.xlabel("Senior Citizen Status")
    plt.ylabel("Count")
    plt.title("Gender Distribution by Senior Citizen")
    plt.xticks(x, gender_senior.index)
    plt.legend()

    for bars in [bars1, bars2]:
        for bar in bars:
            plt.text(
                bar.get_x() + bar.get_width()/2,
                bar.get_height(),
                int(bar.get_height()),
                ha='center',
                va='bottom'
            )

    plt.tight_layout()
    plt.show()


# =========================
# Churn vs Categorical Feature
# =========================
def plot_churn_vs_feature(df, feature, title):
    pd.crosstab(df[feature], df['Churn']).plot(kind='bar', figsize=(6,4))
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(title)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# =========================
# Monthly Charges vs Churn (Quarterly)
# =========================
def plot_monthly_charges_quarter(df):
    df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
    df['MonthlyCharges_Quarter'] = pd.qcut(
        df['MonthlyCharges'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4']
    )

    quarter_churn = pd.crosstab(df['MonthlyCharges_Quarter'], df['Churn'])
    quarter_churn.plot(kind='bar', figsize=(6,4))

    plt.xlabel("Monthly Charges Quarter")
    plt.ylabel("Number of Customers")
    plt.title("Monthly Charges vs Churn")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# =========================
# Tenure Distribution
# =========================
def plot_tenure_distribution(df):
    plt.figure(figsize=(6,4))
    plt.hist(df['tenure'], bins=30)
    plt.xlabel("Tenure (Months)")
    plt.ylabel("Frequency")
    plt.title("Customer Tenure Distribution")
    plt.tight_layout()
    plt.show()


# =========================
# Tenure vs Churn
# =========================
def plot_tenure_vs_churn(df):
    df.boxplot(column='tenure', by='Churn', figsize=(5,4))
    plt.title("Tenure vs Churn")
    plt.suptitle("")
    plt.xlabel("Churn")
    plt.ylabel("Tenure")
    plt.tight_layout()
    plt.show()


# =========================
# Gender vs Internet Service
# =========================
def plot_gender_vs_internet(df):
    pd.crosstab(df['gender'], df['InternetService']).plot(
        kind='bar', figsize=(7,4)
    )
    plt.xlabel("Gender")
    plt.ylabel("Number of Customers")
    plt.title("Gender vs Internet Service Type")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot_churn_vs_sim_operator(df):
    churn_sim = pd.crosstab(df['SIM_Operator'], df['Churn'])

    churn_sim.plot(kind='bar', figsize=(7, 5))

    plt.xlabel("SIM Operator")
    plt.ylabel("Number of Customers")
    plt.title("Churn Distribution by SIM Operator")
    plt.xticks(rotation=0)

    # Add value labels
    for container in plt.gca().containers:
        plt.bar_label(container)

    plt.tight_layout()
    plt.show()



def main():
    df = load_data("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df = add_sim_operator_column(df)

    # ✅ FINAL CHECK (THIS WILL WORK)
    logger.info(df.columns)
    logger.info(df[['SIM_Operator']].head())
    logger.info(df['SIM_Operator'].value_counts())

    # =========================

    # Debug check (must work)
    logger.info(df[['SIM_Operator']].head())
    logger.info(df['SIM_Operator'].value_counts())
    save_dataset(df, "Telco_Customer_Churn_with_SIM.csv")

    plot_churn_distribution(df)
    plot_gender_distribution(df)
    plot_gender_senior(df)
    plot_churn_vs_feature(df, 'gender', "Churn by Gender")
    plot_churn_vs_feature(df, 'Contract', "Churn by Contract Type")
    plot_monthly_charges_quarter(df)
    plot_tenure_distribution(df)
    plot_tenure_vs_churn(df)
    plot_gender_vs_internet(df)
    plot_churn_vs_sim_operator(df)


if __name__ == "__main__":
    main()
