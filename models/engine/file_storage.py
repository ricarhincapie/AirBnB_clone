#!/usr/bin/env python3

import json
from os import path

class FileStorage():
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return self.__objects

	def new(self, obj):
		self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

	def save(self):
		with open(self.__file_path, mode='w') as a_file:
			json.dump(self.__objects, a_file, indent=4, sort_keys=True, default=str)
	
	def reload(self):
		if path.isfile(self.__file_path):
			with open(self.__file_path, mode='r') as a_file:
				self.__objects = json.load(a_file)
	