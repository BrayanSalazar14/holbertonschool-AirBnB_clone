import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
