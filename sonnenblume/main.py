import uvicorn
from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from . import models
from .database import SessionLocal, engine
from .test import view as test_view

load_dotenv()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(test_view.router)
def start_with_poetry():
    uvicorn.run("sonnenblume.main:app", host="0.0.0.0", port=8000, reload=True)

