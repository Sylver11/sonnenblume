import uvicorn
from fastapi import FastAPI #, Depends
from .database import Base, engine
from .test import view as test_view
from .account import views as account_view



Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(test_view.router)
app.include_router(account_view.router)


def start_with_poetry():
    uvicorn.run("sonnenblume.main:app", host="0.0.0.0", port=8000, reload=True)

