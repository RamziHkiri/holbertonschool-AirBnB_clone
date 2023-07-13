#!/usr/bin/python3
"""define the BaseModel class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """defile the base model methods and fields"""

    def __init__(self, *args, **kwargs):
        """the base model constructor"""

        if kwargs and type(kwargs) == dict and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "id":
                        setattr(self, key, value)
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new()

    def __str__(self) -> str:
        """string representation of base model"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """update the time of the model"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """dictionnary representation"""

        diction = self.__dict__.copy()
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = self.created_at.isoformat()
        diction["updated_at"] = self.updated_at.isoformat()
        return diction
