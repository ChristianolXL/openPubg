import cmd, sys

class openPubgShell(cmd.Cmd):
    '''
    A simple command line interface for the openPubg server
    The user can create, manage, delete rooms or players through
    command
    '''

    intro = 'Welcome to the openPubg Shell\n'
    prompt = 'openPubg>> '
    file = None

    def do_echo(self, arg):
        print(arg)

    def do_quit(self, arg):
        return True
