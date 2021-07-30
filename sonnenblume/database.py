from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sonnenblume import config


engine = create_async_engine(str(config.SQLALCHEMY_DATABASE_URI))
async_session = sessionmaker(engine, expire_on_commit=False,class_=AsyncSession)
Base = declarative_base()





#from sqlalchemy import create_engine
#from sqlalchemy.orm import declarative_base, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
#database = databases.Database(str(config.SQLALCHEMY_DATABASE_URI))
#metadata = sqlalchemy.MetaData()
#engine = sqlalchemy.create_engine(
#    DATABASE_URL, connect_args={"check_same_thread": False}
#)
