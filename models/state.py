#!/usr/bin/python3
"""Module that defines a class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
