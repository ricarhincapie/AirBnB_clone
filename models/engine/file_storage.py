#!/usr/bin/env python3

import json
from os import path
from models.base_model import BaseModel
from datetime import datetime
from models.user import User

class FileStorage():
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return self.__objects

	def new(self, obj):
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		self.__objects[key] = obj

	def save(self):
		temp_dict = {}
		for item in self.__objects:
			temp_dict[item] = self.__objects[item].to_dict()

		with open(self.__file_path, 'w', encoding="UTF-8") as a_file:
			json.dump(temp_dict, a_file)
	
	def reload(self):
		if path.isfile(self.__file_path):
			with open(self.__file_path, mode='r') as a_file:
				all_objs = json.load(a_file)

			for obj_id in all_objs.keys():
				class_name = all_objs[obj_id]["__class__"]
				self.__objects[obj_id] = eval(class_name)(**all_objs[obj_id])
