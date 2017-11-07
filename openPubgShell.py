import cmd
import logging
import sys

class openPubgShell(cmd.Cmd):
    '''
    A simple command line interface for the openPubg server
    The user can create, manage, delete rooms or players through
    command
    '''

    intro = 'Welcome to the openPubg Shell\n'
    prompt = 'openPubg>> \n'
    file = None

    def setRoomManager(self, rManager):
        self.roomManager = rManager

    def setTextManager(self, tManager):
        self.textManager = tManager

    def do_echo(self, arg):
        ''' Echo '''
        print(arg)

    def do_list(self):
        ''' List all current rooms '''
        pass

    def do_stop(self, arg):
        ''' Stop a current room '''
        pass

    def do_send(self, arg):
        ''' Send message to user '''
        email = input('Please enter email: ')
        text = input('Please enter message: ')

        message = self.textManager.sendMessage(email, text)

        if message is None:
            print('Send message failed')
        else:
            print('Send message with id %s' %(message['id']))

    def do_info(self, arg):
        ''' Show logging info '''
        logging.basicConfig(level=logging.INFO)

    def do_quit(self, arg):
        self.roomManager.close()
        self.textManager.close()
        return True