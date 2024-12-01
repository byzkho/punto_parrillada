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
    RECEPCIONISTA = "recepcionista"
    COCINERO = "cocinero"
    CLIENTE = "cliente"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(UserRole, values_callable=lambda x: [e.value for e in x]), default=UserRole.CLIENTE)
    is_active = Column(Boolean, default=False)
    full_name = Column(String)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "role": self.role.value,
            "is_active": self.is_active,
            "full_name": self.full_name
        }
    
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    menus = relationship("Menu", back_populates="category")
    
class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    dishes = relationship("Dish", back_populates="menu")
    category = relationship("Category", back_populates="menus")
    
class Dish(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey("menus.id"))
    name = Column(String, unique=True, index=True)
    price = Column(Float)
    description = Column(String)
    size = Column(String, nullable=True)
    menu = relationship("Menu", back_populates="dishes")
    
class TableStatus(enum.Enum):
    LIBRE = "LIBRE"
    OCUPADO = "OCUPADO"
    RESERVADA = "RESERVADA"

class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(TableStatus), default=TableStatus.LIBRE)
    capacity = Column(Integer)
    seats = relationship("Seat", back_populates="table")
    
class Seat(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    table_id = Column(Integer, ForeignKey("tables.id"))
    table = relationship("Table", back_populates="seats")

class UserReservation(Base):
    __tablename__ = "user_reservations"
    id = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(Integer, ForeignKey("reservations.id"))
    receptionist_id = Column(Integer, ForeignKey("users.id"))
    reception_time = Column(DateTime, nullable=True)
    waiter_id = Column(Integer, ForeignKey("users.id"))
    waiter_time = Column(DateTime, nullable=True)
    payment_time = Column(DateTime, nullable=True)

class OrderStatus(enum.Enum):
    PENDIENTE = "pendiente"
    PREPARANDO = "preparando"
    LISTO = "listo"
    SERVIDO = "servido"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(Integer, ForeignKey("reservations.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDIENTE)
    waiter_id = Column(Integer, ForeignKey("users.id"))
    order_items = relationship("OrderItem", back_populates="order")
    
class OrderSeat(Base):
    __tablename__ = "order_seats"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    seat_id = Column(Integer, ForeignKey("seats.id"))
    order = relationship("Order")
    seat = relationship("Seat")
    
class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    seat_id = Column(Integer, ForeignKey("seats.id"))
    product_id = Column(Integer, ForeignKey("dishes.id"))
    quantity = Column(Integer)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDIENTE)
    order = relationship("Order", back_populates="order_items")
    
class ReservationStatus(enum.Enum):
    RESERVADA = "reservada"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservation_time = Column(DateTime)
    arrival_time = Column(DateTime, nullable=True)
    status = Column(Enum(ReservationStatus), default=ReservationStatus.RESERVADA)
    receptionist_id = Column(Integer, ForeignKey("users.id"), nullable=True)

class Bill(Base):
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    total_amount = Column(Float)
    split = Column(Boolean, default=False)
    is_payed = Column(Boolean, default=False)
    order = relationship("Order")
    bill_share = relationship("BillShare", back_populates="bill")
    
class BillShare(Base):
    __tablename__ = "bill_shares"
    id = Column(Integer, primary_key=True, index=True)
    bill_id = Column(Integer, ForeignKey("bills.id"))
    full_name = Column(String)
    amount = Column(Float)
    bill = relationship("Bill")
    
class TokenTable(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now())