#!/usr/bin/python3
""" Console module creates a command-line console to manage HBNB DB
"""

import sys
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand is the class to generate a command-line console
    for the HBNB project
    """
    prompt = "(hbnb) "
    valid_class = ["BaseModel", "User", "Place",
                   "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program.
        Arguments:
        quit
        """
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program.
        Arguments:
        EOF
        """
        print("", end="")
        sys.exit()

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create command to create a new object based on a class name.
        Arguments:
        create [Class name]
        """
        if len(arg) <= 0:
            print("** class name missing **")
        else:
            arg = arg.split()[0]
            if arg in self.valid_class:
                new_obj = eval(arg)()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Show prints an specific object information.
        Arguments:
        show [Class name] [Object Id]
        """
        if len(arg) <= 0:
            print("** class name missing **")
        else:
            arguments = arg.split()
            if len(arguments) == 1:
                if arguments[0] not in self.valid_class:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                if arguments[0] not in self.valid_class:
                    print("** class doesn't exist **")
                else:
                    objects = models.storage.all()
                    try:
                        print(objects[arguments[0] + "." + arguments[1]])
                    except Exception:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy deletes a object.
        Arguments:
        destroy [Class name] [Object Id]
        """
        if len(arg) <= 0:
            print("** class name missing **")
        else:
            arguments = arg.split()
            if arguments[0] not in self.valid_class:
                print("** class doesn't exist **")
            else:
                if len(arguments) == 1:
                    print("** instance id missing **")
                else:
                    objects = models.storage.all()
                    try:
                        key = arguments[0] + "." + arguments[1]
                        del objects[key]
                        models.storage.save()
                        models.storage.reload()
                    except Exception:
                        print("** no instance found **")

    def do_all(self, arg):
        """All prints all current objects created in the system's DB.
        Arguments:
        all - prints all objects in all clases
        all [Class] - prints all objects of the same class
        """
        my_arr = []
        if len(arg) > 0:
            if arg.split()[0] in self.valid_class:
                my_dict = models.storage.all()
                for key, value in my_dict.items():
                    if key.split(".")[0] == arg.split()[0]:
                        my_arr.append(str(value))
                print(my_arr)
            else:
                print("** class doesn't exist **")
        else:
            my_dict = models.storage.all()
            for key, value in my_dict.items():
                my_arr.append(str(value))
            print(my_arr)

    def do_update(self, arg):
        """Update updates an object's attributes
        Arguments:
        update [Class name] [Object's id] [Attribute name] [Attribute value]
        """
        arguments = arg.split()
        my_dict = models.storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) == 1:
            cls_name = arguments[0]
            if cls_name not in self.valid_class:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arguments) == 2:
            cls_name = arguments[0]
            if cls_name not in self.valid_class:
                print("** class doesn't exist **")
            else:
                my_id = arguments[1]
                if cls_name+"."+my_id not in my_dict:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
        elif len(arguments) == 3:
            cls_name = arguments[0]
            if cls_name not in self.valid_class:
                print("** class doesn't exist **")
            else:
                print("** value missing **")
        else:
            cls_name = arguments[0]
            if cls_name not in self.valid_class:
                print("** class doesn't exist **")
            else:
                my_id = arguments[1]
                attr_name = arguments[2]
                attr_val = arg.split("\"")[1]
                if cls_name+"."+my_id not in my_dict:
                    print("** no instance found **")
                else:
                    if hasattr(eval(cls_name), attr_name):
                        temp_attr = getattr(eval(cls_name), attr_name)
                        my_type = eval(type(temp_attr).__name__)
                        if my_type is int:
                            attr_val = int(float(attr_val))
                        key = cls_name+"."+my_id
                        setattr(my_dict[key], attr_name, my_type(attr_val))
                    else:
                        key = cls_name+"."+my_id
                        setattr(my_dict[key], attr_name, attr_val)
                    models.storage.save()
    def default(self, line):
        my_class  = line.split(".")[0]
        my_method = line.split(".")[1]
        if my_method == "all()":   
            my_array = []
            my_dict = models.storage.all()
            for key in my_dict.keys():
                tmp_key = key.split(".")[0]
                if tmp_key == my_class:
                    my_array.append(str(my_dict[key]))
            print(my_array)
        if my_method == "count()":
            suma = 0
            my_dict = models.storage.all()
            for key in my_dict.keys():
                tmp_key = key.split(".")[0]
                if tmp_key == my_class:
                    suma += 1
            print(suma)
        else:
            print("", end="")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
