from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# 1. CẤU HÌNH DATABASE
SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class NoteDB(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, index=True)
    content = Column(Text)

Base.metadata.create_all(bind=engine)

# 2. KHỞI TẠO FASTAPI
app = FastAPI()

# Cấu hình CORS cho phép Frontend gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. PYDANTIC SCHEMAS
class NoteCreate(BaseModel):
    user_email: str
    content: str

class NoteResponse(BaseModel):
    id: int
    user_email: str
    content: str

    class Config:
        orm_mode = True

# Dependency lấy DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 4. CÁC ENDPOINTS
@app.get("/")
def read_root():
    return {"message": "Welcome to Note API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/notes", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = NoteDB(user_email=note.user_email, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes", response_model=list[NoteResponse])
def get_notes(user_email: str, db: Session = Depends(get_db)):
    notes = db.query(NoteDB).filter(NoteDB.user_email == user_email).all()
    return notes 


@app.get("/auth/me")
def get_current_user_info(email: str):
    return {"status": "authenticated", "user_email": email}