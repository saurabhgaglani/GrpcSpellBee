import requests
import json

from requests.api import get


def getWords(): 
    #Getting a list of words from the Github API
    res = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json')
    data = res.json()
    return data


