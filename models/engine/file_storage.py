#!/usr/bin/env python3
"""File storage module creates the methods to save HBNB changes in a
temporary file
"""

import json
from os import path
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """FileStorage class for HBNB data management
    It has a __objects dictionary as a temporary data storage that
    keeps track of current objects available in the program.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all returns all the data stored.
        """
        return self.__objects

    def new(self, obj):
        """New method creates a new object's key and inserts it along with its
        values to the __objects dictionary for it to be file
        storaged and loaded.
        It is called from the BaseModel __init__ method, from a "storage"
        instance originated in the package __init__.py file.
        Arguments:
        new(obj)
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save converts the __objects content into key-value parameters in a
        temporary dictionary. Then it encodes to JSON and saves it in a file.
        """
        temp_dict = {}
        for item in self.__objects:
            temp_dict[item] = self.__objects[item].to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as a_file:
            json.dump(temp_dict, a_file)

    def reload(self):
        """Reloads converts JSON data to program Objects.
        It makes sure a JSON file exists and if positive it opens the file
        and loads the JSON data.
        It copies the __class__ value inside each JSON data's key to
        instantiate it in __objects dictionary along with its attributes.
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path, mode='r') as a_file:
                all_objs = json.load(a_file)

            for obj_id in all_objs.keys():
                class_name = all_objs[obj_id]["__class__"]
                self.__objects[obj_id] = eval(class_name)(**all_objs[obj_id])
