import streamlit as st
import sqlite3
from collections import Counter

st.set_page_config(
    page_title="Security Log Analyzer",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Security Log Analyzer")
st.write("Monitor failed login attempts and security alerts.")

# Read log file
failed_events = []

with open("sample.log", "r") as file:
    for line in file:
        if "FAILED" in line:
            parts = line.split()

            date = parts[0]
            time = parts[1]
            username = parts[3].replace("username=", "")
            ip = parts[4].replace("ip=", "")

            failed_events.append({
                "Date": date,
                "Time": time,
                "Username": username,
                "IP Address": ip
            })

# Count failed attempts
ip_count = Counter(event["IP Address"] for event in failed_events)

# Dashboard numbers
total_attempts = len(failed_events)
suspicious_ips = len([ip for ip, count in ip_count.items() if count >= 3])
high_alerts = len([ip for ip, count in ip_count.items() if count >= 5])

col1, col2, col3 = st.columns(3)

col1.metric("Total Failed Attempts", total_attempts)
col2.metric("Suspicious IPs", suspicious_ips)
col3.metric("High Severity Alerts", high_alerts)

st.subheader("📊 Failed Login Summary")

summary = []

for ip, attempts in ip_count.items():
    if attempts >= 5:
        severity = "HIGH"
    elif attempts >= 3:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    summary.append({
        "IP Address": ip,
        "Failed Attempts": attempts,
        "Severity": severity
    })

st.dataframe(summary, use_container_width=True)

st.subheader("🚨 Security Alerts")

alerts = []

for item in summary:
    if item["Severity"] in ["HIGH", "MEDIUM"]:
        alerts.append({
            "IP Address": item["IP Address"],
            "Attempts": item["Failed Attempts"],
            "Severity": item["Severity"],
            "Reason": "Multiple failed login attempts"
        })

if alerts:
    st.dataframe(alerts, use_container_width=True)
else:
    st.success("No suspicious activity detected.")

st.subheader("🗄️ Saved Alerts in Database")

try:
    conn = sqlite3.connect("security_logs.db")

    cursor = conn.cursor()
    cursor.execute("""
        SELECT ip, username, attempts, severity, time, reason
        FROM alerts
    """)

    rows = cursor.fetchall()
    conn.close()

    database_alerts = []

    for row in rows:
        database_alerts.append({
            "IP Address": row[0],
            "Username": row[1],
            "Attempts": row[2],
            "Severity": row[3],
            "Time": row[4],
            "Reason": row[5]
        })

    st.dataframe(database_alerts, use_container_width=True)

except Exception as e:
    st.error(f"Database error: {e}")