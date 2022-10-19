import string
import random
import grpc
import threading
from concurrent import futures

from pika import channel
import spellbee_pb2
import spellbee_pb2_grpc
import logging
from dict_lookup import *
import pika

randomlist = []
min_word_length = 4

#Connecting to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='winner')



#This class will be deployed on the server along with the dict_lookup script.
class Server(spellbee_pb2_grpc.ServerServicer):

    def __init__(self):
        self.players = []
        self.gameOver = False
        self.winner = ""
        self.i = 0
        self.chosenwordlist = []
        pass    

    #Send list of random letters to the client.
    def getLetters(self, request, context):
        alphabetList = list(string.ascii_uppercase)
        alphabetList.remove('S')
        randomList = random.sample(alphabetList, 7)
        return spellbee_pb2.letterResponse(numbers = randomList)

     #Checks to see if word is valid 
    def checkWord(self, request, context):
        s = Server()
        request.input = str.upper(request.input)
        if(len(request.input) < min_word_length):
            return False
        else:
            for i in request.input:
                if i not in request.num:
                    return spellbee_pb2.wordResponse(res = 'False')
            if(request.input not in self.chosenwordlist):
                if(s.checkDict(request.input) == True):
                    self.chosenwordlist.append(request.input)
                    return  spellbee_pb2.wordResponse(res = 'True')
                else:
                    return  spellbee_pb2.wordResponse(res = 'False')
            else:
                 return  spellbee_pb2.wordResponse(res = 'False')

    
    #If word is valid, this method checks dictionary to see if it is a real word.
    def checkDict(self, input):
        x = dict_lookup()
        wordlist = list(x.getWords().keys())
        if(str.lower(input) in wordlist):
            return True
        else:
            return False

        #Get score of word if the word is valid.
    def getScore(self, request, context):

        if len(request.input) == 4:
            score = len(request.input) - (min_word_length-1)
        else:
            score = len(request.input)
        return spellbee_pb2.scoreResponse(score = score)

    #Send a list of current players to the client.
    def getCurrentState(self, request, context):
        return spellbee_pb2.stateResponse(players = self.players)

    #Find out from client if game has ended or not.
    def gameHasEnded(self, request, context):
        self.gameOver = request.gameOver
        return spellbee_pb2.gameResponse(empty = "")

    #Tell client if game has ended.
    def hasGameEnded(self, request, context):
        return spellbee_pb2.endResponse(gameIsOver = self.gameOver)
    
    #Sets winner
    def declareWinner(self, request, context):
        self.winner = request.winner
        if(request.winner != ""):
            #Send name of the winner and a list of the names of players on server to a queue.
            try:
                channel.basic_publish(exchange='',
                            routing_key='winner',
                            body= f'{{"winner": {self.winner}, "players": {self.players}}}')
                print(f'sent {self.winner}')
            except:
                print("Error")
        return spellbee_pb2.winnerResponse(empty = "")
    
    #Sends name of winner to client.
    def getWinner(self, request, context):
        return spellbee_pb2.getWinnerResponse(winner = self.winner)

    def getNumGames(self, request, context):
        return spellbee_pb2.getGameresponse(games = self.i)



    #Add new player
    def connect(self, request, context):
        print(f'adding player {request.name}')
        self.players.append(request.name)
        self.i+= 1
        print(self.players)
        return spellbee_pb2.connectResponse() 



#Setting up the server.
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spellbee_pb2_grpc.add_ServerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("*****************GAME SERVER STARTED*****************")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()