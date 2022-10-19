import spellbee_pb2_grpc
import spellbee_pb2
import grpc
from spellbee_pb2 import Player
from spellbee_pb2 import gameResponse
import time


#Setting up channel for client and server to communicate on.
channel = grpc.insecure_channel('localhost:50051') 
stub = spellbee_pb2_grpc.ServerStub(channel)
rlist = stub.getLetters(spellbee_pb2.letterRequest(empty = "")).numbers
#print(rlist)

def main():
    gmode = int(input("Select game mode:\nSingle Player - Press 1\nPlay against friend - Press any number key; "))
    if(gmode == 1):
        print(rlist)
        splayerscore = 0
        while input != KeyboardInterrupt:
            word = input("\n Enter Word - ")

            if stub.checkWord(spellbee_pb2.wordRequest(num=rlist, input=word)).res == 'True':
                splayerscore += stub.getScore(spellbee_pb2.scoreRequest(input = word)).score
                print(f'Score = {splayerscore}')
            else:
                print("Word Invalid")

    else:
        name = input("\nName: ")
        score = 0
        player1 = Player(name = name, score = 0)
        stub.connect(player1)
        

        

        while(len(stub.getCurrentState(spellbee_pb2.stateRequest(empty = "")).players) % 2 == 1):
            print("Waiting for player to join...", end = "\r")
            time.sleep(1)

        i = stub.getNumGames(spellbee_pb2.getGameRequest(empty = "")).games
        p1name = stub.getCurrentState(spellbee_pb2.stateRequest(empty = "")).players[i-1]
        p0name = stub.getCurrentState(spellbee_pb2.stateRequest(empty = "")).players[i-2]
        if(name == p0name):
            print(f'\nPlaying against {p1name}')
        else:
            print(f'\nPlaying against {p0name}')


        print(rlist)
        while (score < 2 and stub.hasGameEnded(spellbee_pb2.endRequest(empty = "")).gameIsOver == False):
            word = input("\n Enter Word - ")
            if stub.checkWord(spellbee_pb2.wordRequest(num=rlist, input=word)).res == 'True':
                score += stub.getScore(spellbee_pb2.scoreRequest(input = word)).score
                print(f'Score = {score}')
            else:
                print("Word Invalid")
                
        stub.gameHasEnded(spellbee_pb2.gameRequest(gameOver = True))
        if(name == p0name and stub.getWinner(spellbee_pb2.getWinnerRequest(empty = "")).winner == ""):
            stub.declareWinner(spellbee_pb2.winnerRequest(winner = p0name))
            print("You Win")
        elif(name == p1name and stub.getWinner(spellbee_pb2.getWinnerRequest(empty = "")).winner == ""):
            stub.declareWinner(spellbee_pb2.winnerRequest(winner = p1name))
            print("You Win")
        elif(name == p0name and stub.getWinner(spellbee_pb2.getWinnerRequest(empty = "")).winner != ""):
            print(f'{p1name} has reached 02 points')
            p0name = ""
            p1name = ""
            stub.declareWinner(spellbee_pb2.winnerRequest(winner = ""))
            stub.gameHasEnded(spellbee_pb2.gameRequest(gameOver = False))
            
        elif(name == p1name and stub.getWinner(spellbee_pb2.getWinnerRequest(empty = "")).winner != ""):
            print(f'{p0name} has reached 02 points')
            print(i)
            p0name = ""
            p1name = ""
            stub.declareWinner(spellbee_pb2.winnerRequest(winner = ""))
            stub.gameHasEnded(spellbee_pb2.gameRequest(gameOver = False))
        else:
            print("Too many players on server")


        
        
                            


main()