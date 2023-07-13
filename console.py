#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """ that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Exit the program"""

        return True

    def do_EOF(self, args):
        """Exit the program by pressing Ctrl+D (EOF)"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""

        pass

    def help_quit(self):
        """Print help message for quit command"""

        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help message for the EOF command"""

        print("Exit the program by pressing Ctrl+D (EOF)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
