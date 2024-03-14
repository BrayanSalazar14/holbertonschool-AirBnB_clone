#!/usr/bin/python3
"""
Module contains the entry point of the command interpreter:
"""
import json
import os.path
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Simple command processor example. """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            data = arg.split()
            if len(data) == 1:
                print("** instance id missing **")
                return
            class_id = data[0] + "." + data[1]
            if class_id not in storage.all().keys():
                print("** no instance found **")
                return
            print(storage.all().values())
            # for key, value in storage.all().items():
            #     if class_id == key:
            #         print(value)
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return
        try:
            data = arg.split()
            if len(data) == 1:
                print("** instance id missing **")
                return
            class_id = data[0] + "." + data[1]
            if class_id in storage.all().keys():
                with open("file.json", "w", encoding="utf-8"):
                    storage.all().pop(class_id)
                    storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        try:
            list_obj = [index.__str__() for index in storage.all().values()]
            print(list_obj)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        try:
            data = arg.split()
            if len(data) == 1:
                print("** instance id missing **")
                return
            elif len(data) == 2:
                print("** attribute name missing **")
                return
            elif len(data) == 3:
                print("** value missing **")
                return
            class_id = data[0] + "." + data[1]
            atrr_name = data[2]
            if class_id not in storage.all().keys():
                print("** no instance found **")
                return
            for key, value in storage.all().items():
                if class_id == key:
                    value.__dict__[atrr_name] = data[3]
                    storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        sys.exit()

    def do_EOF(self, arg):
        """Exit the console"""
        sys.exit()

    def emptyLine(self, arg):
        """Print empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
