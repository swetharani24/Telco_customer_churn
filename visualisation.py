import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Suresh Goud\Documents\Intern\WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
df.info



#   churn distribution
churn_counts = df['Churn'].value_counts()
plt.figure(figsize=(5,6))
plt.bar(churn_counts.index,churn_counts.values)
plt.xlabel("Churn")
plt.ylabel("Number of customers")
plt.title("Churn distribution")
plt.show()


# Gender distribution
gender_counts=df['gender'].value_counts()
plt.figure(figsize=(4,3))
plt.bar(gender_counts.index,gender_counts.values)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")
plt.show()


# Senor citizen distribution
senior_counts=df['SeniorCitizen'].value_counts()
plt.figure(figsize=(4,5))
plt.bar(senior_counts.index,senior_counts.values)
plt.xlabel("Senior Citizen(0=No,1=Yes)")
plt.ylabel("Count")
plt.title("Senior citizen Distribution")
plt.show()


# churn vs gender
churn_gender=pd.crosstab(df['gender'],df['Churn'])
churn_gender.plot(kind='bar')
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Churn by Gender")
plt.show()

# Churn vs Contract Type
churn_contract = pd.crosstab(df['Contract'], df['Churn'])
churn_contract.plot(kind='bar')
plt.xlabel("Contract Type")
plt.ylabel("Count")
plt.title("Churn by Contract Type")
plt.xticks(rotation=15)
plt.show()

# Monthly Charges distribution
plt.figure()
plt.hist(df['MonthlyCharges'], bins=30)
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.title("Monthly Charges Distribution")
plt.show()

# Tenure distribution
plt.figure()
plt.hist(df['tenure'], bins=30)
plt.xlabel("Tenure (Months)")
plt.ylabel("Frequency")
plt.title("Customer Tenure Distribution")
plt.show()

# Churn vs Tenure
df.boxplot(column='tenure', by='Churn')
plt.title("Tenure vs Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Tenure")
plt.show()


#  Internet Service distribution
internet_counts = df['InternetService'].value_counts()

plt.figure()
plt.bar(internet_counts.index, internet_counts.values)
plt.xlabel("Internet Service")
plt.ylabel("Count")
plt.title("Internet Service Distribution")
plt.show()
