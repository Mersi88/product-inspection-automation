from flask import Flask, jsonify, render_template, request
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "..", "cleaned_data.csv")

@app.route("/")
def home():
    df = pd.read_csv(CSV_PATH)

    total_quantity = int(df["quantity"].sum())
    status_counts = df["status"].value_counts().to_dict()

    return render_template(
    "index.html",
    total_quantity=total_quantity,
    status_counts=status_counts
)

@app.route("/api/summary")
def api_summary():
    status_filter = request.args.get("status")

    df = pd.read_csv(CSV_PATH)

    if status_filter:
        df = df[df["status"] == status_filter]

    total_quantity = int(df["quantity"].sum())
    status_counts = df["status"].value_counts().to_dict()

    return jsonify({
        "total_quantity": total_quantity,
        "status_counts": status_counts
    })




if __name__ == "__main__":
    app.run(debug=True)
