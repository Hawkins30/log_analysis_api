from fastapi import FastAPI, Depends
from pydantic import BaseModel
from analyser import analyse_log_lines
from database import Analysis, get_db
from sqlalchemy.orm import Session

app = FastAPI()


class LogInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello world"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyse")
def analyse_logs(data: LogInput, db: Session = Depends(get_db)):
    lines = data.text.splitlines()

    counts, malformed_lines = analyse_log_lines(lines)

    analysis = Analysis(
        counts=counts,
        total_lines=len(lines),
        malformed_lines=malformed_lines
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return {
        "id": analysis.id,
        "counts": counts,
        "total_lines": len(lines),
        "malformed_lines": malformed_lines
    }

@app.get("/analyses")
def get_analyses(db: Session = Depends(get_db)):
    analyses = db.query(Analysis).all()

    return [
        {
            "id": a.id,
            "created_at": a.created_at,
            "counts": a.counts,
            "total_lines": a.total_lines,
            "malformed_lines": a.malformed_lines
        }
        for a in analyses
    ]
