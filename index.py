python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_file = 'Traffic_Accident_Data_Abu_Dhabi_2025.xlsx'
df = pd.read_excel(data_file)

# Data Preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.day_name()

# Analysis Example: Most accident-prone streets
top_streets = df['Street'].value_counts().head(10)

# Visualization: Accidents by Month
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Month', palette='viridis')
plt.title('Number of Accidents by Month in 2025')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.show()

# Visualization: Accidents by Weekday
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Weekday', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='coolwarm')
plt.title('Number of Accidents by Weekday in 2025')
plt.xlabel('Weekday')
plt.ylabel('Number of Accidents')
plt.show()

# Output Top Streets
print("Top 10 Accident-Prone Streets:")
print(top_streets)
