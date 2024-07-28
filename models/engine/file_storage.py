#!/usr/bin/python3
""" file_storge model """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
    """
    serializes instances to JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    __obj_value = {}
    __instance_obj = {}
    def __init__(self):
        pass

    def all(self):
        """  returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[
                f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        objects_json = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            file.write(json.dumps(objects_json))

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                deserialized_obj = json.loads(file.read())
            for key in deserialized_obj.keys():
                FileStorage.__objects[key] = classes[deserialized_obj[key]["__class__"]](**deserialized_obj[key])
        except FileNotFoundError:
            pass
