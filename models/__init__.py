#!/usr/bin/python3
"""init"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

# List of models to be imported when importing from models package
__all__ = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
