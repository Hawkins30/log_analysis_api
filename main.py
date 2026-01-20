from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
import json

from analyser import analyse_log_lines
from database import Analysis, get_db

app = FastAPI()


@app.post("/analyse")
def analyse_logs(payload: dict, db: Session = Depends(get_db)):
    # Ensure table exists (Render + SQLite safe)
    db.execute(text("""
    CREATE TABLE IF NOT EXISTS analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at DATETIME,
        counts TEXT,
        total_lines INTEGER,
        malformed_lines INTEGER
    )
    """))
    db.commit()

    text_data = payload.get("text", "")
    lines = text_data.splitlines()

    counts, malformed_lines = analyse_log_lines(lines)

    analysis = Analysis(
        counts=json.dumps(counts),
        total_lines=len(lines),
        malformed_lines=malformed_lines
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return {
        "id": analysis.id,
        "counts": counts,
        "total_lines": analysis.total_lines,
        "malformed_lines": analysis.malformed_lines
    }


@app.get("/analyses")
def get_analyses(db: Session = Depends(get_db)):
    results = db.query(Analysis).all()

    return [
        {
            "id": a.id,
            "created_at": a.created_at,
            "counts": json.loads(a.counts),
            "total_lines": a.total_lines,
            "malformed_lines": a.malformed_lines
        }
        for a in results
    ]
