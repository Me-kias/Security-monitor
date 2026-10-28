
import sqlite3

DATABASE_FILE = "/mnt/security_alerts.db""


def create_database():
    connection = sqlite3.connect(DATABASE_FILE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_type TEXT NOT NULL,
            source_ip TEXT NOT NULL,
            attempt_count INTEGER NOT NULL,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def save_alert(alert):
    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.execute("""
        INSERT INTO alerts (
            alert_type,
            source_ip,
            attempt_count,
            description
        )
        VALUES (?, ?, ?, ?)
        """, (
            alert["alert_type"],
            alert["source_ip"],
            alert["attempt_count"],
            alert["description"]
        ))
if __name__ == "__main__":
    create_database()
    print("Database and alerts table created successfully!")


def get_alerts():
    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.row_factory = sqlite3.Row

        rows = connection.execute("""
            SELECT * FROM alerts
            ORDER BY id DESC
        """).fetchall()

        return [dict(row) for row in rows]
