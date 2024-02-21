#!/usr/bin/python3
""" A script that defines a new class storage DBStorage"""
import unittest
import os
from models.storage_db import DBStorage
from models.base_model import Base
from models.city import City
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class TestDBStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test environment for the entire class"""
        user = os.getenv("HBNB_MYSQL_USER", "hbnb_test")
        pwd = os.getenv("HBNB_MYSQL_PWD", "hbnb_test_pwd")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        db = "hbnb_test_db"
        cls.engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)
        Base.metadata.create_all(cls.engine)
        Session = sessionmaker(bind=cls.engine)
        cls.session = scoped_session(Session)

    @classmethod
    def tearDownClass(cls):
        """Tear down the test environment for the entire class"""
        cls.session.remove()
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """Set up test environment for each test"""
        self.storage = DBStorage()
        self.storage.__engine = self.engine
        self.storage.__session = self.session()

    def tearDown(self):
        """Tear down test environment for each test"""
        self.storage.__session.rollback()
        self.storage.__session.close()

    def test_all(self):
        """Test all method"""
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIn(f"State.{state.id}", all_objs)
        self.assertIn(f"City.{city.id}", all_objs)

    def test_new(self):
        """Test new method"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        all_objs = self.storage.all(State)
        self.assertIn(f"State.{state.id}", all_objs)

    def test_save(self):
        """Test save method"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        all_objs = self.storage.all(State)
        self.assertIn(f"State.{state.id}", all_objs)

    def test_delete(self):
        """Test delete method"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        self.storage.save()
        all_objs = self.storage.all(State)
        self.assertNotIn(f"State.{state.id}", all_objs)

    def test_reload(self):
        """Test reload method"""
        self.storage.reload()
        self.assertIsNotNone(self.storage.__session)

if __name__ == '__main__':
    unittest.main()