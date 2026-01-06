import pandas as pd
from log_file import setup_logging
logger = setup_logging('feature_encoding')


def load_data(path):
    try:
        df = pd.read_csv(path)
        logger.info(f"Dataset loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        logger.info(f"Error: File not found at path '{path}'")
        return None
    except Exception as e:
        logger.info(f"Error loading data: {e}")
        return None

def drop_columns(df, columns):
    try:
        df.drop(columns=columns, inplace=True)
        logger.info(f"Columns dropped: {columns}")
        return df
    except KeyError as e:
        logger.info(f"Error: Column not found - {e}")
        return df
    except Exception as e:
        logger.info(f"Error dropping columns: {e}")
        return df

def encode_target(df, column, mapping):
    try:
        df[column] = df[column].map(mapping)
        logger.info(f"Target variable '{column}' encoded")
        return df
    except KeyError:
        logger.info(f"Error: Target column '{column}' not found")
        return df
    except Exception as e:
        logger.info(f"Error encoding target: {e}")
        return df


def encode_binary_features(df, binary_cols, mapping_dict):
    try:
        for col in binary_cols:
            df[col] = df[col].map(mapping_dict[col])
        logger.info("Binary features encoded:", binary_cols)
        return df
    except KeyError as e:
        logger.info(f"Error: Column not found - {e}")
        return df
    except Exception as e:
        logger.info(f"Error encoding binary features: {e}")
        return df


# One-hot encode multi-category features
def encode_multi_category(df, multi_cols):
    try:
        df = pd.get_dummies(df, columns=multi_cols, drop_first=True)
        logger.info("Multi-category features one-hot encoded:", multi_cols)
        return df
    except KeyError as e:
        logger.info(f"Error: Column not found - {e}")
        return df
    except Exception as e:
        logger.info(f"Error encoding multi-category features: {e}")
        return df

def save_data(df, filename):
    try:
        df.to_csv(filename, index=False)
        logger.info(f"Encoded dataset saved successfully as '{filename}'")
    except Exception as e:
        logger.info(f"Error saving dataset: {e}")

def main():
    path = "cleaned_telco_churn.csv"
    df = load_data(path)
    if df is None:
        return

    df = drop_columns(df, ['customerID'])

    df = encode_target(df, 'Churn', {'No': 0, 'Yes': 1})

    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    mapping_dict = {
        'gender': {'Female': 0, 'Male': 1},
        'Partner': {'No': 0, 'Yes': 1},
        'Dependents': {'No': 0, 'Yes': 1},
        'PhoneService': {'No': 0, 'Yes': 1},
        'PaperlessBilling': {'No': 0, 'Yes': 1}
    }
    df = encode_binary_features(df, binary_cols, mapping_dict)

    # One-hot encode multi-category features
    multi_cols = ['InternetService', 'Contract', 'PaymentMethod']
    df = encode_multi_category(df, multi_cols)

    logger.info("\nEncoded dataset preview:")
    logger.info(df.head())
    logger.info("\nDataset info:")
    logger.info(df.info())
    logger.info("\nMissing values per column:")
    logger.info(df.isnull().sum())

    save_data(df, "encoded_telco_churn.csv")


if __name__ == "__main__":
    main()
