import pandas as pd
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())
df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].mean())
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
df = df.drop_duplicates()
print("\nAfter cleaning:")
print(df.isnull().sum())
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Cleaning complete! File saved as cleaned_data.csv")