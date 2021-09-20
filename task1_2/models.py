from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app import db


@dataclass
class User(db.Model):
    id: int
    salary: int
    name: str
    data: str

    __tablename__ = 'users_rkorshunov'
    id = Column(Integer, primary_key=True)
    salary = Column(Integer)
    name = Column(String(255))
    data = Column(DateTime)


@dataclass
class House(db.Model):
    id: int
    user_id: int
    address: str
    cost: int

    __tablename__ = 'houses_rkorshunov'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users_rkorshunov.id'))
    address = Column(String(255))
    cost = Column(Integer)
    user = relationship('User')
