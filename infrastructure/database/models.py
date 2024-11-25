from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped, declarative_base
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
    role = Column(Enum(UserRole), default=UserRole.CLIENTE)
    full_name = Column(String)
    avatar = Column(String)
    user_tables = relationship("UserTable", back_populates="user")
    
    
class UserAttendedBy(Base):
    __tablename__ = "user_attended_by"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    attended_by = Column(Integer, ForeignKey("users.id"), primary_key=True)
    attended_at = Column(DateTime)

    user = relationship("User", foreign_keys=[user_id])
    attended_by_user = relationship("User", foreign_keys=[attended_by])

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

    user_tables = relationship("UserTable", back_populates="table")
    
class UserTable(Base):
    __tablename__ = "user_tables"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    table_id = Column(Integer, ForeignKey("tables.id"), primary_key=True)
    reservated_at = Column(DateTime, nullable=True)
    ocuppated_at = Column(DateTime, nullable=True)
    free_at = Column(DateTime, nullable=True)
    user = relationship("User", back_populates="user_tables")
    table = relationship("Table", back_populates="user_tables")
    order = relationship("Order", back_populates="user_table")
class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date_time = Column(DateTime)
    duration = Column(Float, nullable=True)
    table = relationship("Table")
    user = relationship("User")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_table_id = Column(Integer, ForeignKey("user_tables.user_id"))  # Clave correcta
    items = Column(String)  # Lista de pedidos
    status = Column(Boolean, default=False)

    user_table = relationship("UserTable", back_populates="order")


class Bill(Base):
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    total_amount = Column(Float)
    split = Column(Boolean, default=False)  # Divide la cuenta entre personas
    order = relationship("Order")

class TokenTable(Base):
    __tablename__ = "tokens"
    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    