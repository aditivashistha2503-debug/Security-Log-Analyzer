from collections import Counter
import sqlite3

# Connect to database
conn = sqlite3.connect("security_logs.db")
cursor = conn.cursor()

# Create alerts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    username TEXT,
    attempts INTEGER,
    severity TEXT,
    time TEXT,
    reason TEXT
)
""")

conn.commit()

# Store failed login information
failed_ips = []
failed_events = []

# Read log file
with open("sample.log", "r") as file:
    for line in file:

        if "FAILED" in line:
            parts = line.split()

            date = parts[0]
            time = parts[1]
            username = parts[3].replace("username=", "")
            ip = parts[4].replace("ip=", "")

            failed_ips.append(ip)

            failed_events.append({
                "date": date,
                "time": time,
                "username": username,
                "ip": ip
            })

# Count failed attempts
ip_count = Counter(failed_ips)

print("\nFailed Login Summary:")

for ip, attempts in ip_count.items():
    print(ip, "->", attempts, "failed attempts")

# Generate security alerts
print("\nSecurity Alerts:")

for ip, attempts in ip_count.items():

    if attempts >= 5:
        severity = "HIGH"

    elif attempts >= 3:
        severity = "MEDIUM"

    else:
        continue

    # Find username and time
    username = ""
    time = ""

    for event in failed_events:
        if event["ip"] == ip:
            username = event["username"]
            time = event["time"]

    print("\n⚠️ SECURITY ALERT")
    print("Severity:", severity)
    print("IP Address:", ip)
    print("Username:", username)
    print("Attempts:", attempts)
    print("Time:", time)
    print("Reason: Multiple failed login attempts")

    # Check for duplicate alert
    cursor.execute("""
    SELECT id FROM alerts
    WHERE ip = ? AND username = ? AND attempts = ? AND severity = ?
    """, (ip, username, attempts, severity))

    existing_alert = cursor.fetchone()

    if existing_alert is None:

        cursor.execute("""
        INSERT INTO alerts
        (ip, username, attempts, severity, time, reason)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            ip,
            username,
            attempts,
            severity,
            time,
            "Multiple failed login attempts"
        ))

        conn.commit()
        print("Alert saved to database.")

    else:
        print("Alert already exists in database.")

# View saved alerts
print("\nSaved Alerts in Database:")

cursor.execute("SELECT * FROM alerts")
alerts = cursor.fetchall()

for alert in alerts:
    print(alert)

# Close database
conn.close()