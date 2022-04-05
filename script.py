from re import I
from accounts import Users
from messaging import Messages
from termcolor import colored
import time


class Script:
    account_run = Users()  
    personal_qc = None
    quantum_circuits = None
    runtime = Messages()
    def __init__(self):
        
        while True:
            user_prompt = str(input(': '))
            if user_prompt == '/sign_up':
                initial_run = self.account_run.sign_up()
                if initial_run == False:
                    print(colored('You have exited the Signing up Process', 'cyan'))
                else:
                    print(colored('Successfully Signed Up', 'green'))
                    time.sleep(0.2)
                    print(colored('You can now proceed to sign in', 'white'))
                    continue
            elif user_prompt == '/sign_in':
                self.account_run.sign_in()
                try:
                    self.quantum_circuits = {self.account_run.logged_in_user[0]:self.personal_qc}
                except:
                    continue

            
            if self.account_run.signed_in == True:
                self.personal_qc = self.account_run.personal_qc
                if user_prompt == '/email':
                    pass 
                elif user_prompt == '/sgc':         # Send global chat         
                    self.runtime.sending_message(self.account_run.logged_in_user[0], self.personal_qc, self.quantum_circuits)
                elif user_prompt == '/send_email':
                    self.runtime.send_email(personal_qc=self.personal_qc)
            else:
                print(colored("You are not signed in yet!", 'red'))

        
        




test = Script()
