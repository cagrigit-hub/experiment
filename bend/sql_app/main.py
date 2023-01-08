from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "https://localhost:3000",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/lectures/", )
def create_user(db: Session = Depends(get_db)):
    print(db)
    db_lec = crud.create_lecture(db)
    if db_lec:
        raise HTTPException(status_code=400, detail="Email already registered")
    return True

@app.get("/lectures/", response_model=List[schemas.Lecture])
def read_lectures( db: Session = Depends(get_db)):
    lectures = crud.get_lectures(db)
    return lectures


@app.delete("/lectures/")
def delete_lectures( db: Session = Depends(get_db)):
    crud.clear_lectures(db)
    return True