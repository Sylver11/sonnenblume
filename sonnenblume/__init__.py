import uvicorn
from fastapi import FastAPI, Depends
from functools import lru_cache
from . import config
from .database import SessionLocal, engine
from . import models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@lru_cache()
def get_settings():
    return config.Settings()

@app.get("/info")
async def info(settings: config.Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }

def main():
    uvicorn.run("sonnenblume:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
