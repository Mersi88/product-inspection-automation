import pandas as pd

# Load raw data
df = pd.read_csv("data/raw_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["quantity"] = df["quantity"].fillna(0)
df["inspector"] = df["inspector"].fillna("Unknown")

# Convert quantity to integer
df["quantity"] = df["quantity"].astype(int)

# Analysis
total_quantity = df["quantity"].sum()
status_counts = df["status"].value_counts()

print("Total Quantity Inspected:", total_quantity)
print("\nInspection Status Counts:")
print(status_counts)

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)
