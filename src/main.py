import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data():
    df = pd.read_csv("data/raw_data.csv")
    df = df.drop_duplicates()
    df["quantity"] = df["quantity"].fillna(0).astype(int)
    df["inspector"] = df["inspector"].fillna("Unknown")
    return df

def analyze_data(df):
    total_quantity = df["quantity"].sum()
    status_counts = df["status"].value_counts()
    return total_quantity, status_counts

def save_outputs(df):
    df.to_csv("data/cleaned_data.csv", index=False)

def generate_chart(status_counts):
    status_counts.plot(kind="bar")
    plt.title("Inspection Status Summary")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("data/status_summary.png")
    plt.close()

def generate_report(total_quantity, status_counts):
    with open("data/report.txt", "w") as file:
        file.write("Inspection Summary Report\n")
        file.write("-------------------------\n")
        file.write(f"Total Quantity Inspected: {total_quantity}\n\n")
        file.write("Status Counts:\n")
        file.write(status_counts.to_string())

def main():
    while True:
        print("\nProduct Inspection Automation Tool")
        print("1. Run full analysis")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            df = load_and_clean_data()
            total_quantity, status_counts = analyze_data(df)

            print("\n--- Inspection Summary ---")
            print("Total Quantity Inspected:", total_quantity)
            print("\nStatus Counts:")
            print(status_counts)

            save_outputs(df)
            generate_chart(status_counts)
            generate_report(total_quantity, status_counts)

            print("\nOutputs generated successfully.")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
