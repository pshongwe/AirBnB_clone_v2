#!/usr/bin/python3
"""Module that defines a class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class that inherits from BaseModel"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
