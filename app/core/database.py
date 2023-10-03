from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, Session

from app.core.config import DatabaseConfiguration

sqlalchemy_metadata = MetaData()


class Model(DeclarativeBase):
    metadata = sqlalchemy_metadata
    
engine = create_engine(DatabaseConfiguration.SQLITE, connect_args={"check_same_thread": False})

def create_tables_and_db(engine):
    Model.metadata.create_all(bind=engine)


async def db_session() -> Session:
    with Session(bind=engine) as session:
        yield session
        
    
