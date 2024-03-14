#!/usr/bin/python3
"""
Module contains the entry point of the command interpreter:
"""
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
        try:
            data = arg.split()
            if len(data) == 0:
                print("** instance id missing **")
                return
            class_id = data[0] + "." + data[1]
            for key, value in storage.all().items():
                if class_id == key:
                    print(value)
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
