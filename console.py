#!/usr/bin/python3
""" console """


import cmd
import re
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ TODO: document """
    prompt = "(hbnb) "
    __list_of_class = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
    dot = "."
    o_bracket = "("
    c_bracket = ")"

    """def postcmd(self, stop, line):
        Hook method executed just after a command dispatch is finished.
        cmd, arg, rest_line = super().parseline(line)
        print(cmd)
        print(arg)
        print(rest_line)
        if cmd in HBNBCommand.__list_of_class:
            eval(arg[0][1:])
        return stop"""
    
    def onecmd(self, line):
        """Interpret the argument as though it had been typed in response
        to the prompt.

        This overridden, but should not normally need to be;
        see the precmd() and postcmd() methods for useful execution hooks.
        The return value is a flag indicating whether interpretation of
        commands by the interpreter should stop.
        """

        ## ToDo: refactor this for readability
        cmd, arg, line = super().parseline(line)
        if not line:
            return super().emptyline()
        if cmd is None:
            return super().default(line)
        self.lastcmd = line
        if line == 'EOF' :
            self.lastcmd = ''
        if cmd == '':
            return super().default(line)
        else:
            try:
                func = getattr(self, 'do_' + cmd)
            except AttributeError:
                i, n = 0, len(line)
                while i < n and line[i] not in self.dot: i = i+1
                custom_cmd = line[0:i]
                custom_arg = line[i:].strip()
                try:
                    j , k = 0 , len(custom_arg)
                    while j < k and custom_arg[j] not in self.o_bracket:j = j+1
                    pattern = re.compile("\(.*\)")
                    arg_call = line[j+i:]
                    matches =  re.match(pattern, arg_call)
                    if not matches:
                        return super().default(line)
                    x , y = 1, len(arg_call)
                    while x < y and arg_call[x] not in self.c_bracket: x = x+1
                    #arg_call = arg_call[0+1:x].split(",")
                    arg_call = re.split(r',(?![^{}]*\})',  arg_call[1:x])
                    arg_call[0] = arg_call[0].replace("\"", '')
                    arg_str = ""
                    for arg in arg_call : arg_str = arg_str + arg + " "
                    arg_str = arg_str.strip()
                    cmd = custom_arg[0+1:j]
                    arg = custom_cmd + " " + arg_str
                    func = getattr(self, "do_" + custom_arg[0+1:j])
                    #func(f"{custom_cmd}")
                except:
                        return super().default(line)
            return func(arg)

    def do_create(self, arg):
        """ TODO: document """
        try:
            args = arg.split()
            if len(args) > 1:
                print ("** too many argumets **")
                return
            if not args:
                print("** class name missing **")
            else:
                if args[0] in HBNBCommand.__list_of_class:
                    #instance = globals()[args[0]]()
                    for cls in HBNBCommand.__list_of_class:
                        if cls == args[0]:
                            instance = eval(cls)()
                    instance.save()
                    print(instance.id)
                else:
                    print("** class doesn't exist **")
        except ValueError:
            print("** class name missing **")

    def do_show(self, arg):
        """ TODO: document """
        storage_objects = storage.all()
        try:
            args = arg.split()
            if len(args) > 2:
                print ("** too many argumets **")
                return
            if not args:
                print("** class name missing **")
            elif not args[0]:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                if args[0] not in HBNBCommand.__list_of_class:
                    print("** class doesn't exist **")
                else:
                    print(args[1])
                    if f"{args[0]}.{args[1]}" not in storage_objects:
                        print("** no instance found **")
                    else:
                        print(storage_objects[f"{args[0]}.{args[1]}"])
        except ValueError:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ TODO: document """
        storage_objects = storage.all()
        try:
            args = arg.split()
            if len(args) > 2:
                print ("** too many argumets **")
                return
            if not args:
                print("** class name missing **")
            elif not args[0]:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                if args[0] not in HBNBCommand.__list_of_class:
                    print("** class doesn't exist **")
                else:
                    if f"{args[0]}.{args[1]}" not in storage_objects:
                        print("** no instance found **")
                    else:
                        del storage_objects[f"{args[0]}.{args[1]}"]
                        storage.save()
        except ValueError:
            print("** class name missing **")

    def do_all(self, arg):
        """ TODO: Document """
        storage_objects = storage.all()
        try:
            args = arg.split()
            if len(args) > 1:
                print ("** too many argumets **")
                return
            if args[0] in HBNBCommand.__list_of_class:
                all_arg_obj = []
                for value in storage_objects.values():
                    if value.__class__.__name__ == args[0]:
                        all_arg_obj.append(value.__str__())
                print(all_arg_obj)
            else:
                print("** class doesn't exist **")
        except IndexError:
            print([value.__str__() for value in storage_objects.values()])


    def do_update(self, arg):
        """ TODO: doc """
        storage_objects = storage.all()
        try:
            try:
                args = re.split(r' (?![^{}]*\})', arg)
                args = [arg.strip() for arg in args if arg != '']
            except re.error as e:
                print(e)
            if not args:
                print("** class name missing **")
            elif not arg[0]:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                if args[0] not in HBNBCommand.__list_of_class:
                    print("** class doesn't exist **")
                else:
                    if f"{args[0]}.{args[1]}" not in storage_objects:
                        print("** no instance found **")
                    else:
                        obj = storage_objects[f"{args[0]}.{args[1]}"]
                        if len(args) < 3:
                            print("** attribute name missing **")
                        try:
                            dict_value = eval(args[2])
                            if type(eval(args[2])) is dict:
                                obj.__dict__.update(dict_value)
                                obj.save()
                                return
                        except:
                            pass
                        if len(args) < 4:
                            print("** value missing **")
                        else:
                            att_name = args[2].replace("\"", "").replace("'", "")
                            try:
                                att_val = eval(args[3])
                            except SyntaxError:
                                print("** value missing **")
                                return
                            obj.__dict__.update({att_name: att_val})
                            obj.save()
        except ValueError:
            print("** class name missing **")

    def do_count(self, arg):
        """ TODO: Document """
        storage_objects = storage.all()
        try:
            args = arg.split()
            if len(args) > 1:
                print ("** too many argumets **")
                return
            if args[0] in HBNBCommand.__list_of_class:
                all_arg_obj = []
                for value in storage_objects.values():
                    if value.__class__.__name__ == args[0]:
                        all_arg_obj.append(value.__str__())
                print(len(all_arg_obj))
            else:
                print("** class doesn't exist **")
        except IndexError:
            print(len([value.__str__() for value in storage_objects.values()]))

    def do_quit(self, arg):
        """ Quit the cmd """
        return True

    def do_EOF(self, arg):
        """ exit when signal End Of File """
        print("")
        return True

    def help_quit(self):
        """ document  quit command """
        print("Quit command to exit the program")

    def help_EOF(self):
        """ document EXIT THE CMD """
        print("quit due to CTRL+D")

    def emptyline(self):
        """ do nothing when empty string """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
