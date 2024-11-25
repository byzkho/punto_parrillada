import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

load_dotenv()

url = f"sqlite:///{os.environ.get('DB_TEST_NAME')}"

engine = create_engine(url, echo=False)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_manager = scoped_session(session)

get_session = lambda: session_manager

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()