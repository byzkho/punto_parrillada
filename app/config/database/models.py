from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from .database import Base
import enum

"""class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True)  # libre, ocupada, reservada
    capacity = Column(Integer)"""

class UserRole(enum.Enum):
    ADMIN = "admin"
    RECEPCION = "recepcion"
    MESERO = "mesero"
    CAJERO = "cajero"

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(UserRole), default=UserRole.CAJERO)

class TableStatus(enum.Enum):
    LIBRE = "libre"
    OCUPADA = "ocupada"
    RESERVADA = "reservada"

class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True)
    status = Column(Enum(TableStatus), default=TableStatus.LIBRE)
    seats = Column(Integer)

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date_time = Column(DateTime)
    duration = Column(Float)  # Duración en horas
    table = relationship("Table")
    user = relationship("User")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    items = Column(String)  # Lista de pedidos
    status = Column(Boolean, default=False)
    table = relationship("Table")

class Bill(Base):
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    total_amount = Column(Float)
    split = Column(Boolean, default=False)  # Divide la cuenta entre personas
    order = relationship("Order")
