from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# DB URL is "database://username:password@localhost:PORT/database_name"
db_url = "postgresql://postgres:postgres@localhost:5432/fastapi1"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
