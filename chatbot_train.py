#from chatterbot import ChatBot
from simple_websocket_server import WebSocketServer, WebSocket
"""from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('C:/Users/Prathmesh/Desktop/Python/Chatbot_Project-master/data/'):
        convData = open(r'C:/Users/Prathmesh/Desktop/Python/Chatbot_Project-master/data/' + file,encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        #print("Training completed")
    

setup()
"""