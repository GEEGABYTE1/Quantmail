from re import I
from accounts import Users
from messaging import Messages
from termcolor import colored
import time


class Script:
    account_run = Users()
    personal_qc = None
    runtime = Messages()
    def __init__(self):
        
        while True:
            user_prompt = str(input(': '))
            if user_prompt == '/sign_up':
                self.account_run.sign_up()
                print(colored('Successfully Signed Up', 'green'))
                time.sleep(0.2)
                print(colored('You can now proceed to sign in', 'white'))
                continue
            elif user_prompt == '/sign_in':
                self.account_run.sign_in()

            
            if self.account_run.signed_in == True:
                self.personal_qc = self.account_run.personal_qc
                if user_prompt == '/email':
                    pass 
                elif user_prompt == '/sgc':         # Send global chat         
                    self.runtime.sending_message(self.account_run.logged_in_user[0], self.personal_qc)
                elif user_prompt == '/send_email':
                    pass
            else:
                print(colored("You are not signed in yet!", 'red'))

        
        




test = Script()
