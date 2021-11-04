from generate_puzzle import *


rlist = getLetters()
print(rlist)

def checkInput():
    word = input("\n Enter Word - ")
    if(checkWord(rlist, word) == True):
        score = getScore(word)
        print(f'Score = {score}')
    else:
        print("Word too short")


def main():
    while input != KeyboardInterrupt:
        checkInput()
    print(score)

main()
