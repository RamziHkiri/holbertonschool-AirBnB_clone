#!/usr/bin/python3
"""define the class file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """define the file storage methods and fields"""

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = ("{}.{}".format(type(obj).__name__, obj.id))
        FileStorage.__objects[obj_key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dictionary = {}
            for key, value in FileStorage.__objects.items():
                dictionary[key] = value.to_dict()
            f.write(json.dumps(dictionary))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    cls = FileStorage.class_dict[cls_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
