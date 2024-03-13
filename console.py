#!/usr/bin/python3
"""
Module contains the entry point of the command interpreter:
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Simple command processor example. """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """Exit the console"""
        sys.exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
