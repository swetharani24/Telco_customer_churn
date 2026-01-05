import pandas as pd

df = pd.read_csv("cleaned_telco_churn.csv")
print("Dataset loaded")
df.drop(columns=['customerID'], inplace=True)
print("customerID column dropped")
df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})
print("Target variable encoded")
binary_cols = [
    'gender', 'Partner', 'Dependents',
    'PhoneService', 'PaperlessBilling'
]
for col in binary_cols:
    df[col] = df[col].map({'No': 0, 'Yes': 1, 'Female': 0, 'Male': 1})

print("Binary features encoded")
multi_cols = [
    'InternetService',
    'Contract',
    'PaymentMethod'
]
df = pd.get_dummies(df, columns=multi_cols, drop_first=True)
print("Multi-category features one-hot encoded")
print(df.head())
print(df.info())
print(df.isnull().sum())
df.to_csv("encoded_telco_churn.csv", index=False)
print("Encoded dataset saved successfully")
