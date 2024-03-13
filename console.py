import cmd
"""
Module contains the entry point of the command interpreter:
"""


class HBNBCommand(cmd.Cmd):
    """
    Simple command processor example.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
