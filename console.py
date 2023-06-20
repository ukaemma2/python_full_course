import cmd

class HBNBCommand(cmd.Cmd):
    
    def  do_quit(self):
        return True
    
    def do_EOF(self):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()