from sqlalchemy import create_engine
from app.config.database.database import Base
from app.config.database.config import settings


engine = create_engine(settings.database_url)

def init_db():
    Base.metada.create_all(bind=engine)
    
if __name__ == "__main__":
    init_db()