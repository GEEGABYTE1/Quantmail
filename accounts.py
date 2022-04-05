from pymongo import MongoClient
from termcolor import colored
import time
import certifi
from qiskit import QuantumCircuit

qcs = []

class Users:
    cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
    db = cluster['socialmedia']['accounts']
    qc_db = cluster['socialmedia']['qc']
    qc_db.insert_one({})
    all_accounts = db.find({})
    signed_in = False
    logged_in_user = None
    personal_qc = None
    user_user = None
    sign_up_run = False

    def sign_up(self):
        user_name = str(input("Please enter a username you would like to go by (Note: Users externally will see this name): "))
        password = str(input("Please enter a password: "))
        if user_name == '/quit' or password == '/quit':
            return False
        acc = {'User': user_name, 'Password': password, 'Inbox':[]}
        qcs.append({user_name:QuantumCircuit(2, 2)}) 
        qcs[0][user_name].h(1)
        qcs[0][user_name].cx(1, 0)
        self.personal_qc = qcs[0][user_name]
        #all_qcs = self.qc_db.find({})
        #self.qc_db.insert_one({'Name':user_name})
        self.db.insert_one(acc)
        self.sign_up_run = True
        return True

    def sign_in(self):
        while True:
            user = str(input("Username: "))
            
            users = []
            passwords = []
            for account in self.all_accounts:
                users.append(account['User'])
                passwords.append(account['Password'])
            if user == '/quit':
                    break

            if user in users:
                while True:
                    password = str(input("Password: "))
                    
                    if password == '/quit':
                        break
                    elif password in passwords:
                        self.signed_in = True 
                        if self.sign_up_run == False:
                            self.logged_in_user = [user, password, []]
                            established_circuit = QuantumCircuit(2, 2)
                            established_circuit.h(1)
                            established_circuit.cx(1, 0)
                            self.personal_qc = established_circuit
                            print(colored('Circuit Added', 'cyan'))
                            print(colored("You have successfully signed in! ", 'green'))
                            break
                    else:
                        print("Password is incorrect")

                if self.signed_in == False:
                    print("You have left the logging in process...")
                else:
                    break


            else:
                print(colored("That username does not seem to be registered on this network", 'red'))
                time.sleep(0.2)
                print(colored("Try signing up to the network!", 'blue'))
        
        if self.signed_in == False:
            print("You have left the logging in process...")
        
        return self.signed_in
                

            


        
    
    
user = Users()
