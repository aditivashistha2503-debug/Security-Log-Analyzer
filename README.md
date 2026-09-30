# 🔐 Security Log Analyzer

## 1. Project Overview

Security Log Analyzer is a Python-based cybersecurity project that analyzes login logs and detects repeated failed login attempts.

The project identifies suspicious IP addresses, assigns severity levels, stores security alerts in an SQLite database, and displays the results through a Streamlit dashboard.

## 2. Objectives

- Analyze security log files
- Detect repeated failed login attempts
- Identify suspicious IP addresses
- Generate security alerts
- Assign HIGH and MEDIUM severity levels
- Store alerts in an SQLite database
- Display results using a web dashboard

## 3. Technologies Used

- Python
- Streamlit
- SQLite
- VS Code

## 4. How It Works

1. The program reads the `sample.log` file.
2. It detects failed login attempts.
3. Failed attempts are counted for each IP address.
4. IPs with repeated failures are classified as suspicious.
5. Security alerts are generated.
6. Alerts are stored in `security_logs.db`.
7. The Streamlit application displays the results in a dashboard.

## 5. Severity Levels

| Failed Attempts | Severity |
|---|---|
| 5 or more | HIGH |
| 3–4 | MEDIUM |
| Less than 3 | LOW |

## 6. Project Files

- `main.py` – analyzes logs and stores security alerts
- `app.py` – displays the Streamlit dashboard
- `sample.log` – sample security log data
- `security_logs.db` – SQLite database containing alerts
- `README.md` – project documentation

## 7. Dashboard Features

- Total failed login attempts
- Suspicious IP detection
- Severity classification
- Failed login summary
- Security alerts
- Saved database alerts
- Downloadable summary

## 8. Result

The project successfully detects repeated failed login attempts and displays the detected security information through an interactive dashboard.

## 9. Conclusion

The Security Log Analyzer demonstrates how Python, log analysis, SQLite, and Streamlit can be combined to create a simple cybersecurity monitoring system.