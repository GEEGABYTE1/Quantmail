from re import I
from accounts import Users
from messaging import Messages
from termcolor import colored
import time


class Script:
    account_run = Users()
    personal_qc = account_run.personal_qc
    def __init__(self):

        while True:
            user_prompt = str(input(': '))
            if user_prompt == '/sign_up':
                self.account_run.sign_up()
                print(colored('Successfully Signed Up', 'green'))
                time.sleep(0.2)
                print(colored('You can now proceed to sign in', 'white'))
            elif user_prompt == '/sign_in':
                self.account_run.sign_in()
            
            else:
                print(colored('Incorrect Command'))
            
            if self.account_run.signed_in == True:
                if user_prompt == '/email':
                    pass 
                elif user_prompt == '/sgc':         # Send global chat
                    runtime = Messages()
                    runtime.sending_message(self.account_run.logged_in_user[0], self.personal_qc)
                elif user_prompt == '/send_email':
                    pass
            else:
                print(colored("You are not signed in yet!", 'red'))

        
        




test = Script()
