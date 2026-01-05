import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Suresh Goud\Documents\Intern\WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.shape
df.info()
df.duplicated().sum()
df=df.drop_duplicates()
print(df.drop_duplicates())

# check missing values
df.isnull().sum()
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')

print("Total charges converted to numeric")
df.isnull().sum()



# missing values
df=df.dropna()
#  fill null values with median
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
print("\nMissing values AFTER handling:")
print(df.isnull().sum())

# checking categorical columns
df.select_dtypes(include='object').nunique()
print(df.select_dtypes)


# check categorical columns
df.describe()
print(df)

# finding outliers

# monthly charges
plt.boxplot(df['MonthlyCharges'])
plt.title('Monthly Charges Outliers')
plt.show()


# tenure
plt.boxplot(df['tenure'])
plt.title('Tenure Outliers')
plt.show()


# Total charges
plt.boxplot(df['TotalCharges'])
plt.title('Total Charges Outliers')
plt.show()

df['Churn'].value_counts()

print(df)
df.info()
# Shape after cleaning
print("\nShape after cleaning:", df.shape)
df.to_csv("cleaned_telco_churn.csv", index=False)
print("Cleaned dataset saved!")





