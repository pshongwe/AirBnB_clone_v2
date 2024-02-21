#!/usr/bin/python3
"""Module that defines class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Colum, String, Integer, Float, ForeignKey
from models.user import User
from models.city import City


class Place(BaseModel, Base):
    """Place class that inherits from BaseModel"""
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable+True)
