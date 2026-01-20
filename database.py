from sqlalchemy import create_engine, Column, Integer, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
DATABASE_URL = "sqlite:////tmp/database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    counts = Column(Text)
    total_lines = Column(Integer)
    malformed_lines = Column(Integer)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
