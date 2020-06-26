#!/usr/bin/env python3

import uuid
import datetime
import models

class BaseModel():
	def __init__(self, *args, **kwargs):
		if not kwargs:
			self.id = str(uuid.uuid4())
			self.updated_at = datetime.datetime.now()
			self.created_at = datetime.datetime.now()
			models.storage.new(self)
		else:
			for charac in kwargs:
				if charac != "__class__":
					if charac == "updated_at" or charac == "created_at":
						value = datetime.datetime.strptime(
							kwargs[charac], "%Y-%m-%dT%H:%M:%S.%f"
							)
						setattr(self, charac, value)
					else:
						setattr(self, charac, kwargs[charac])
	def __str__(self):
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		self.updated_at = datetime.datetime.now()
		models.storage.save()

	def to_dict(self):
		dic = self.__dict__
		dic["__class__"] = self.__class__.__name__
		dic["created_at"] = dic["created_at"].isoformat()
		dic["updated_at"] = dic["updated_at"].isoformat()
		return dic
