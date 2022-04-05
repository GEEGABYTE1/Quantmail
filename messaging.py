import certifi
from datetime import datetime
from sympy import Quaternion
from termcolor import colored
from pymongo import MongoClient
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit import Aer




cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = cluster['socialmedia']['messaging']
all_messages = db.find({})
chats = {}
restart = False


class Messages:

    def sending_message(self, user, personal_qc):
        while True:
            date = datetime.now().strftime("%x")
            for message in self.all_messages:
                try:
                    if date != message['Date']:
                        print(colored('Today: {}'.format(message['Time']), 'red'))
                    else:
                        print(colored("{} ~ {}".format(message['Date'], message['Time']), "red"))
                    print(colored("From: ", 'green'), message['Id'])
                    sender_qc = message['qc']
                    message = message['Message']
                    # Quantum Decryption
                    message_dict = self.untangle(sender_qc, personal_qc)
                    decrypted_message = list(message_dict.keys())[0]

                    print(colored("Message: {}".format(decrypted_message), 'green'))
                    print('-'*25)
                except:
                    pass
            
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
                msg = {"Id": person, "Message": message, "Date": date, "Time":time}
                # Quantum Encryption Here




                
                self.db.insert_one(msg)
                print(colored('Message sent successfully', 'green'))
                print('-'*25)

    

    def untangle(self, resulting_qc, your_qc):
        your_qc.cx(0, 1)
        your_qc.h(0)
        your_qc.measure([0, 1], [0, 1])
        backend = Aer.get_back('aer_simulator')
        resulting_dictionary = backend.run(resulting_qc.compose(your_qc)).result().get_counts()
        return resulting_dictionary
        