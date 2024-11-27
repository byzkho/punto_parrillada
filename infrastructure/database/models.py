# FILE: models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class UserRole(enum.Enum):
    GERENTE = "gerente"
    MESERO = "mesero"
    CAJERO = "cajero"
    SUPERVISOR = "supervisor"
    COCINERO = "cocinero"
    CLIENTE = "cliente"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(UserRole, values_callable=lambda x: [e.value for e in x]), default=UserRole.CLIENTE)
    full_name = Column(String)
    avatar = Column(String)
    sessions = relationship("Session", back_populates="user")
    
class TableStatus(enum.Enum):
    LIBRE = "LIBRE"
    OCUPADO = "OCUPADO"
    RESERVADA = "RESERVADA"

class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True)
    status = Column(Enum(TableStatus), default=TableStatus.LIBRE)
    seats = Column(Integer)
    sessions = relationship("Session", back_populates="table")

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservated_at = Column(DateTime, nullable=True)
    ocuppated_at = Column(DateTime, nullable=True)
    free_at = Column(DateTime, nullable=True)
    user = relationship("User", back_populates="sessions")
    table = relationship("Table", back_populates="sessions")
    orders = relationship("Order", back_populates="session")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    items = Column(String)  # Lista de pedidos
    status = Column(Boolean, default=False)
    session = relationship("Session", back_populates="orders")

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date_time = Column(DateTime)
    quantity = Column(Integer)
    table = relationship("Table")
    user = relationship("User")

class Bill(Base):
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    total_amount = Column(Float)
    split = Column(Boolean, default=False)  # Divide la cuenta entre personas
    order = relationship("Order")

class TokenTable(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now())