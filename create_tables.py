from infrastructure.database.database import engine
from infrastructure.database.models import Base

def create_tables():
    """Crea las tablas en la base de datos."""
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas en la base de datos.")

if __name__ == "__main__":
    create_tables()