import sqlite3

DB_NAME = "database/app.db"

def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT,
            platform TEXT,
            tone TEXT,
            caption TEXT,
            image_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


def save_campaign(prompt, platform, tone, caption, image_url):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO campaigns
        (prompt, platform, tone, caption, image_url)
        VALUES (?, ?, ?, ?, ?)
        """,
        (prompt, platform, tone, caption, image_url)
    )

    conn.commit()
    conn.close()


def get_campaigns():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, prompt, platform, tone, caption, image_url, created_at
        FROM campaigns
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return rows