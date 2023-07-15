#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Define the command methods"""

    prompt = '(hbnb) '
    classes = {
        "BaseModel", "State", "City", "Amenity", "Place", "Review", "User"
    }

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

    def do_create(self, args):
        """Create instance specified by the user"""
        if not args:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            cls = getattr(models, args)
            instance = cls()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """Print string representation: name and id"""
        if not args:
            print("** class name missing **")
            return
        args = self.parse(args)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, args):
        """Destroy instance specified by user; Save changes to JSON file"""
        if not args:
            print("** class name missing **")
            return
        args = self.parse(args)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, args):
        """Print all objects or all objects of specified class"""
        args = self.parse(args)
        obj_list = []
        if not args:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in self.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update if given exact object, exact attribute"""
        args = self.parse(args)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, args):
        """Display count of instances specified"""
        if args in self.classes:
            count = 0
            for key, objs in storage.all().items():
                if args in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, args):
        """Accepts class name followed by argument"""
        args = args.split('.')
        class_arg = args[0]
        if class_arg not in self.classes:
            print("*** Unknown class: {}".format(class_arg))
            return

    def parse(self, args):
        """Helper method to parse user-typed input"""
        return tuple(args.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
