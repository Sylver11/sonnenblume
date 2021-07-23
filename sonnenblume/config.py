from pydantic import BaseSettings
import dotenv

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = 'hellllo'
    items_per_user: int = 50

    class Config:
        env_file = ".env"

