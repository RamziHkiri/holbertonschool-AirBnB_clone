#!/usr/bin/python3
"""define the class file storage"""
import json


class FileStorage:
    """define the file storage methods and fields"""

    __file_path = ""
    __objects = {}

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
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                data = json.loads(f.read())
                for key in data.keys():
                    value = data[key]
                    FileStorage.__objects[key] = eval(
                        value["__class__"])(**value)
                return FileStorage.__objects
        except IOError:
            return{}
