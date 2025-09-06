from fastapi import FastAPI, Request
import psycopg2
import os
from datetime import datetime

app = FastAPI()

DATABASE_URL = os.environ['DATABASE_URL']

@app.post("/api/upload")
async def upload(request: Request):
    data = await request.json()
    message = data.get('message')
    tag = data.get('tag')

    if not message or not tag:
        return {"error": "Missing data"}, 400

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (message, tag, timestamp) VALUES (%s, %s, %s)",
        (message, tag, datetime.now())
    )
    conn.commit()
    cur.close()
    conn.close()

    return {"status": "uploaded"}
