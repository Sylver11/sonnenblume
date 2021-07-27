from starlette.config import Config


from pydantic import BaseSettings
#from dotenv import load_dotenv

#load_dotenv()
#
class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = 'hellllo'
    items_per_user: int = 50

    class Config:
        env_file = ".env"


config = Config(".env")
#settings = AppSettings()#settings = AppSettings()

SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
