#!/usr/bin/env python3

import sys
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "

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
			if arg == "BaseModel":
				new_obj = BaseModel()
				models.storage.save()
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
				if arguments[0] != "BaseModel":
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
			if arguments[0] != "BaseModel":
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

if __name__ == "__main__":
	HBNBCommand().cmdloop()
