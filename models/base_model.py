#!/usr/bin/env python3
"""
Base Model module defines the BaseModel class, its attributes
and methods.
"""
import uuid
import datetime
import models


class BaseModel():
    """BaseModel is the main class for this program.
    It defines the __init__ method for all the program objects
    """
    def __init__(self, *args, **kwargs):
        """__init__ defines instantiation method.
        """
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
        """__str__ method returns a object's string representation.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Save method saves current __objects content to JSON file.
        It calls a method inside file_storage.py.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict methods takes an BaseModel instance __dict__
        meth and converts it to the standard format for the
        program.
        It also changes timestamps formats to fit for JSON
        serialization with isoformat() meth.

        Returns:
        [dic] -- a dictionary ready for JSON serializarion.
        """
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
