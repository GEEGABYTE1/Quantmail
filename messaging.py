from sre_parse import State
import certifi
from datetime import datetime
from sympy import Quaternion
from termcolor import colored
from pymongo import MongoClient
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit import Aer
from accounts import qcs




cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = cluster['socialmedia']['messaging']
qc_db = cluster['socialmedia']['qc']
account_db = cluster['socialmedia']['accounts']

chats = {}
restart = False





class Messages:

    def sending_message(self, user, personal_qc):
        while True:
            names = []
            all_messages = db.find({})
            for message in all_messages:
                name = message['Id']
                name = name.strip('Name: ')
                names.append(name)
            date = datetime.now().strftime("%x")
            all_messages = db.find({})
            all_qcs = qc_db.find({})
            for message in all_messages:    
                #try:
                    if date != message['Date']:
                        print(colored('Today: {}'.format(message['Time']), 'red'))
                    else:
                        print(colored("{} ~ {}".format(message['Date'], message['Time']), "red"))
                    print(colored("From: ", 'green'), message['Id'])
                    name_split = message['Id'].strip('Name: ')
                    message = message['Id']
                            

                            
                    # Quantum Decryption
                    message_dict = self.untangle(personal_qc)
                    decrypted_message = list(message_dict.keys())[0]

                    print(colored("Message: {}".format(decrypted_message), 'green'))
                    print('-'*25)
                #except:
                    #pass
            
            person = "Name: {}".format(user)
            message = input("Message: ")
            message = message.strip(' ')
            if message == '/quit':
                break
            elif message == '/update':
                self.restart()
            elif len(message) > 2:
                print('Message is too long')
            else:
                time = datetime.now().strftime("%X")
                new_message = self.decrypt(personal_qc, message)
                msg = {"Id": person, "Message": new_message, "Date": date, "Time":time}
                
                db.insert_one(msg)
                print(colored('Message sent successfully', 'green'))
                print('-'*25)

    def fetch_users(self):
        names_in_order = []
        count = 0
        for param in account_db:
            name = param['Id']
            names_in_order.append({name: count})
            count += 1

        return names_in_order
        

    def send_email(self, personal_qc):
        desired_user = str(input("Please type in the Desired User: "))
        
    
    def decrypt(self, personal_qc, message):
        if message[-2] == '1':
            personal_qc.x(1)
            message[-2] = '0'
        if message[-1] == '1':
            personal_qc.z(1)
        

        ket = Statevector(personal_qc)
        ket.draw()
        return message



    def untangle(self, personal_qc):
        resulting_qc = QuantumCircuit(2, 2)
        resulting_qc.cx(0, 1)
        resulting_qc.h(0)
        resulting_qc.measure([0, 1], [0, 1])
        backend = Aer.get_back('aer_simulator')
        resulting_dictionary = backend.run(personal_qc.compose(resulting_qc)).result().get_counts()
        return resulting_dictionary
        