import pandas as pd

import warnings
warnings.filterwarnings('ignore')
from log_file import setup_logging

logger = setup_logging("datacleaning")


def load_data(path):
    try:
        df = pd.read_csv(path)
        logger.info(f"Dataset loaded successfully. Shape: {df.shape}")
        return df

    except FileNotFoundError:
        logger.error(f"File not found at path: {path}")
        return None

    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return None


def data_overview(df):
    logger.info(f"Duplicate rows: {df.duplicated().sum()}")
    logger.info("Missing values:")
    logger.info(df.isnull().sum())


def clean_data(df):
    df = df.drop_duplicates()

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

    logger.info("Missing values after cleaning:")
    logger.info(df.isnull().sum())

    return df


def categorical_analysis(df):
    logger.info("Categorical columns unique values:")
    logger.info(df.select_dtypes(include="object").nunique())


def statistical_summary(df):
    logger.info("Statistical summary:")
    logger.info(df.describe())


def churn_distribution(df):
    logger.info("Churn distribution:")
    logger.info(df["Churn"].value_counts())


def save_cleaned_data(df, filename):
    df.to_csv(filename, index=False)
    logger.info(f"Cleaned dataset saved as {filename}")


def main():
    path = r"C:\Users\Suresh Goud\Documents\Intern\WA_Fn-UseC_-Telco-Customer-Churn.csv"

    df = load_data(path)
    if df is None:
        return

    data_overview(df)
    df = clean_data(df)
    categorical_analysis(df)
    statistical_summary(df)
    churn_distribution(df)

    logger.info(f"Final dataset shape: {df.shape}")
    save_cleaned_data(df, "cleaned_telco_churn.csv")


if __name__ == "__main__":
    main()
