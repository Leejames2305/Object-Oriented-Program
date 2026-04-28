# ========== Assesment 2 ==========
# Student Name 1    : Lee Xin Yi
# Student ID 1      : 2103307
# Student Programme : MH
#  
# Student Name 2    : Chua Yun Juan
# Student ID 2      : 2103232
# Student Programme : MH
# ====================================

# %%
import pandas as pd
import matplotlib.pyplot as plt

# Load the csv datasets and merge them
df1 = pd.read_csv('sales_q1.csv')
df2 = pd.read_csv('sales_q2.csv')
df3 = pd.read_csv('sales_q3.csv')
df4 = pd.read_csv('sales_q4.csv')
df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Create revenue column and multiply price with quantity
df['revenue'] = df['price'] * df['quantity']

# Summary of data just after merging, before data cleaning
print("Summary of data after data merging:")
print("-" * 50)
print(f"Total Transactions: {len(df)}")
print(f"Total Revenue: ${df['revenue'].sum():,.2f}")
print(f"Average Revenue: ${df['revenue'].mean():,.2f}")

# Data Cleaning, remove rows with missing values in any column
# Remove duplicate rows, retain first occurrence
# Remove rows with price or quantity less than or equal to zero
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df = df[(df['price'] > 0) & (df['quantity'] > 0)]

# Summary of data after data cleaning
print("\nSummary of data after data cleaning:")
print("-" * 50)
print(f"Total Transactions: {len(df)}")
print(f"Total Revenue: ${df['revenue'].sum():,.2f}")
print(f"Average Revenue: ${df['revenue'].mean():,.2f}")


# %%
# Visualisation
# Histogram showing price distribution to understand spread of product prices
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, color="#bacad6", edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.5)
plt.grid(axis='x', alpha=0.5)
plt.show()

# Line Chart showing total revenue by month (Jan-Dec), Display value for each month clearly
df['month'] = pd.to_datetime(df['date']).dt.month
monthly_revenue = df.groupby('month')['revenue'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue['month'], monthly_revenue['revenue'], marker='o', color='orange')
plt.title('Total Revenue by Month')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(range(1, 13))
plt.grid(axis='y', alpha=0.5)
plt.grid(axis='x', alpha=0.5)
for i, value in enumerate(monthly_revenue['revenue']):
    plt.text(monthly_revenue['month'][i], value, f'${value:,.2f}', ha='center', va='bottom', fontsize=8, bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
plt.show()
 

# %%