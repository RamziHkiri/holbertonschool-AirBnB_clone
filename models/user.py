#!/usr/bin/python3
"""define the user model"""
from models.base_model import BaseModel


class User(BaseModel):
    """define user methods and fields"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
