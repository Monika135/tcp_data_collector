import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()

engine = create_engine(
    os.environ["SQLALCHEMY_DATABASE_URI"],
    pool_pre_ping=True,
    max_overflow=20
)

session_factory = sessionmaker(bind=engine, expire_on_commit=False)
ScopedSession = scoped_session(session_factory)