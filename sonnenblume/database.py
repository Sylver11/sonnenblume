from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sonnenblume import config


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

#import sqlalchemy
#import databases


#database = databases.Database(str(config.SQLALCHEMY_DATABASE_URI))
#
#metadata = sqlalchemy.MetaData()
#engine = sqlalchemy.create_engine(
#    DATABASE_URL, connect_args={"check_same_thread": False}
#)



engine = create_engine(str(config.SQLALCHEMY_DATABASE_URI))
async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
