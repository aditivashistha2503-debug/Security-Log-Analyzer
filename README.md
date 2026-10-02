# 🔐 Security Log Analyzer

A Python-based cybersecurity project that analyzes failed login attempts and detects suspicious IP addresses.

## 📌 Project Overview

Security Log Analyzer is a security monitoring application built using Python, Streamlit, and SQLite.

It analyzes login logs, counts failed login attempts, identifies suspicious IP addresses, and generates security alerts when multiple failed login attempts are detected.

## 🚀 Features

- Analyzes failed login attempts
- Identifies suspicious IP addresses
- Assigns alert severity
- Generates security alerts
- Stores alerts in SQLite database
- Displays results through an interactive Streamlit dashboard
- Shows failed login summaries and saved alerts

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Git & GitHub

## 📊 Dashboard

The dashboard displays:

- Total Failed Attempts
- Suspicious IPs
- High Severity Alerts
- Failed Login Summary
- Security Alerts
- Saved Alerts in Database

## ▶️ How to Run

1. Clone the repository:

git clone https://github.com/aditivashistha2503-debug/Security-Log-Analyzer.git

2. Open the project folder:

cd Security-Log-Analyzer

3. Install Streamlit:

pip install streamlit

4. Run the dashboard:

python -m streamlit run app.py
