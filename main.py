from fastapi import FastAPI
from pydantic import BaseModel
from analyser import analyse_log_lines

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
def analyse_logs(data: LogInput):
    lines = data.text.splitlines()

    counts, malformed_lines = analyse_log_lines(lines)

    return {
        "counts": counts,
        "total_lines": len(lines),
        "malformed_lines": malformed_lines
    }
