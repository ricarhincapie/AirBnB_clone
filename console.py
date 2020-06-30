#!/usr/bin/env python3
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
                print("** instance id missing **")
            else:
                if arguments[0] not in self.valid_class:
                    print("** class doesn't exist **")
                else:
                    objects = models.storage.all()
                    try:
                        print(objects[".".join(arguments)])
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
                        del objects[".".join(arguments)]
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
            if arg in self.valid_class:
                my_dict = models.storage.all()
                for key, value in my_dict.items():
                    if key.split(".")[0] == arg:
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
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
