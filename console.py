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
            if len(data) == 1:
                print("** instance id missing **")
                return
            id = data[1]
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        sys.exit()

    def do_EOF(self, arg):
        """Exit the console"""
        sys.exit()

    def do_emptyLine(self, arg):
        """Print empty line"""
        print("\n")
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
