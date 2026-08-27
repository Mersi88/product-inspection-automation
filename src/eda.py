import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "..", "cleaned_data.csv")

df = pd.read_csv(csv_path)



# Basic overview
print("Dataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Status distribution
status_counts = df["status"].value_counts()

plt.figure()
status_counts.plot(kind="bar")
plt.title("Inspection Status Distribution")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_distribution.png")
plt.close()

# Quantity by status
quantity_by_status = df.groupby("status")["quantity"].mean()

plt.figure()
quantity_by_status.plot(kind="bar")
plt.title("Average Quantity by Inspection Status")
plt.xlabel("Status")
plt.ylabel("Average Quantity")
plt.tight_layout()
plt.savefig("avg_quantity_by_status.png")
plt.close()

print("\nEDA completed. Charts generated.")
