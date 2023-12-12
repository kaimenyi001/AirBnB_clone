#!/usr/bin/python3
"""This is a Method Command Interpretor"""
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, cr):
        '''It Create a new instance of BaseModel, saves it and
            prints the id.
           Usage: create <class name>
        '''

        if cr == "" or cr is None:
            print("**class name missing**")
        elif cr not in models.storage.classes():
            print("**class doesn't exist **")
        else:
            new = models.storage.classes()[cr]()
            new.save()
            print(new.id)

    def do_show(self, args):
        '''It Prints the string representation of a
            specific instance
           Usage: show <class name> <id>
        '''
        strings = args.split()
        if len(strings) == 0:
            print("* Class name is missing *")
        elif strings[0] not in HBNBCommand.__classes:
            print("* Class doesn't exist *")
        elif len(strings) == 1:
            print("* Instance id is missing *")
        else:
            obj = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("* No instance was found *")

    def do_destroy(self, args):
        '''Deletes an instance
           Usage: destroy <class name> <id>
        '''
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('* Class name is missing *')
        elif args[0] not in HBNBCommand.__classes:
            print("* class doesn't exist *")
        elif len(args) == 1:
            print('* Instance id is missing *')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('* No instance was found *')

    def do_all(self, args):
        '''Prints a string representation of all instances
           Usage: all <class name>
        '''
        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj._str_())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("* Class doesn't exist *")
        else:
            for obj in objects.values():
                if obj._class.name_ == args[0]:
                    new_list.append(obj._str_())
            print(new_list)

    def do_update(self, args):
        '''updates an instance
           Usage update <class name> <id> <attribute name> "<attribute value>"
        '''
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("* Class name is missing *")
        elif args[0] not in HBNBCommand.__classes:
            print("* Class doesn't exist *")
        elif len(args) == 1:
            print("* Instance id is missing *")
        elif len(args) == 2:
            print("* Attribute name is missing *")
        elif len(args) == 3:
            print("* Value is missing *")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("* No instance was found *")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """Check if stdin user typed class name and id."""
        if len(name) == 0:
            print("* Class name is missing *")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Checks class id"""
        if len(name.split(' ')) == 1:
            print("* Instance id is missing *")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("* Class doesn't exist *")
                    return None

    def do_quit(self, args):
        '''<Quit> Command To Exit The Program'''
        return True

    def do_EOF(self, args):
        '''Handles end of file'''
        return True

    def emptyline(self):
        '''dont execute anything when user
           press enter an empty line
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
