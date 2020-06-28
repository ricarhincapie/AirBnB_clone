#!/usr/bin/env python3

import sys
import cmd
from models.base_model import BaseModel
from models.user import User
import models

class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "
	valid_class = ["BaseModel", "User"]
	def do_quit(self, arg):
		"""Quit command to exit the program
		"""        
		sys.exit()

	def do_EOF(self, arg):
		"""EOF command to exit the program
		"""
		sys.exit()

	def emptyline(self):
		pass

	def do_create(self, arg):
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
					except:
						print("** no instance found **")

	def do_destroy(self, arg):
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
					except:
						print("** no instance found **")
	
	def do_all(self, arg):
		my_arr = []
		if len(arg) > 0:
			if arg in self.valid_class:
				my_dict = models.storage.all()
				for key, value in my_dict.items():
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
		arguments = arg.split()
		my_dict = models.storage.all()
		if len(arguments) == 0:
			print("** class name missing **")
			
		elif len(arguments) == 1:
			class_name = arguments[0]
			if class_name not in self.valid_class:
				print("** class doesn't exist **")
			print("** instance id missing **")
		elif len(arguments) == 2:
			class_name = arguments[0]
			my_id = arguments[1]
			if class_name+"."+my_id not in my_dict:
				print("** no instance found **")
			else:
				print("** attribute name missing **") # Id validation pending
		elif len(arguments) == 3:
			print("** value missing **")
		else:
			class_name = arguments[0]
			my_id = arguments[1]
			attribute_name = arguments[2]
			attribute_value = arg.split("\"")[1]
			setattr(my_dict[class_name+"."+my_id], attribute_name, attribute_value)

if __name__ == "__main__":
	HBNBCommand().cmdloop()
