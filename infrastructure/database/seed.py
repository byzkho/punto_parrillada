from database import session_manager
from models import Seat, User, Table, TableStatus
import os
import bcrypt
import json

def run_seeder():
    print("--- Ejecutando seeder ---")
    session = session_manager()

    # Ruta del archivo JSON
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_dir, 'seeder', 'data.json')

    # Cargar datos del JSON
    with open(data_file_path, 'r') as f:
        seed_data = json.load(f)

    # Procesar usuarios
    for user_data in seed_data.get("users", []):
        if 'password' in user_data:
            hashed_password = bcrypt.hashpw(
                user_data['password'].encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')
            user_data['password'] = hashed_password

        user = User(**user_data)
        session.add(user)

    # Procesar mesas
    for table_data in seed_data.get("tables", []):
        if "status" in table_data:
            table_data["status"] = TableStatus[table_data["status"].upper()]

        table = Table(**table_data)
        session.add(table)
        
    for seat_data in seed_data.get("seats", []):
        seat = Seat(**seat_data)
        session.add(seat)

    # Confirmar los cambios
    session.commit()
    print("--- Seeder ejecutado con éxito ---")

if __name__ == "__main__":
    run_seeder()