import certifi
from datetime import datetime
from termcolor import colored
from pymongo import MongoClient




cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = cluster['socialmedia']['messaging']
all_messages = db.find({})
chats = {}
restart = False


class Messages:

    def sending_message(self, user):
        while True:
            date = datetime.now().strftime("%x")
            for message in self.all_messages:
                try:
                    if date != message['Date']:
                        print(colored('Today: {}'.format(message['Time']), 'red'))
                    else:
                        print(colored("{} ~ {}".format(message['Date'], message['Time']), "red"))
                    print(colored("From: ", 'green'), message['Id'])
                    print(colored("Message: ", 'green'), message['Message'])
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
                self.db.insert_one(msg)
                print('-'*25)