# Inspection Data Analysis & Dashboard (Flask)

## Overview
This project demonstrates an end-to-end data workflow using Python. It starts with raw inspection data, performs data cleaning and exploratory analysis using Pandas, and exposes the results through a lightweight Flask web application with a simple interactive dashboard.

The goal of this project is to showcase practical skills across:
data preprocessing → analysis → backend API → frontend visualization.

---

## Features
- Data cleaning and preprocessing using Pandas
- Exploratory Data Analysis (EDA)
- Flask backend with:
  - HTML dashboard
  - JSON API endpoint
- Dynamic inspection status visualization
- Clear separation of data, analysis, and web layers

---

## Tech Stack
- Python
- Pandas, NumPy
- Flask (REST API + HTML dashboard)
- JavaScript (fetch API)
- HTML
- Matplotlib
## Architecture Overview

The application follows a layered full-stack structure:

• Data Layer  
  - Raw inspection data stored as CSV files  
  - Data cleaned and preprocessed using Pandas  

• Backend Layer (Flask API)  
  - Processes cleaned datasets  
  - Provides JSON endpoints for dashboard data  
  - Handles routing between frontend and analysis logic  

• Frontend Layer  
  - HTML dashboard using Flask templates  
  - Displays inspection trends and status distribution visuals  

This design demonstrates separation of concerns and scalable backend-frontend interaction.

## How to Run
```bash
pip install flask pandas
python data/eda_project/web/app.py

