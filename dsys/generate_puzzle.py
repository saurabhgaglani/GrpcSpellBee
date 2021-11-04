import string
import random
import grpc
from requests.api import get

from dict_lookup import getWords

randomlist = []
min_word_length = 4
score = 0




def getLetters():
    alphabetList = list(string.ascii_uppercase)
    alphabetList.remove('S')
    randomList =   random.sample(alphabetList, 7)
    return randomList



def getScore(word):
    if len(word) == 4:
        score = len(word) - (min_word_length-1)
    else:
        score = len(word)
    return score



def checkWord(rlist, input):
    input = str.upper(input)
    if(len(input) < min_word_length):
        return False
    else:
        for i in input:
            if i not in rlist:
                return False
        if(checkDict(input) == True):
            return True



def checkDict(word):
    wordlist = list(getWords().keys())
    if(str.lower(word) in wordlist):
        return True
    else:
        return False



    

    
   

    