from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DATABASE_URL = os.environ['DATABASE_URL']

@app.get("/api/messages")
def get_messages():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT message, tag, timestamp FROM messages ORDER BY timestamp DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [{"message": row[0], "tag": row[1], "timestamp": row[2].isoformat()} for row in rows]
