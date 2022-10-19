import threading
import requests
import json
import threading

from requests.api import get

class dict_lookup:
    instance = None

    def __init__(self):
        pass

    def __init__(self):
        if dict_lookup.instance is not None:
            raise Exception("This is a singleton!")
        else:
            dict_lookup.__instance = self
        self.lock = threading.Lock()
        self.matches = {}
        self.instance = None

    @staticmethod
    def get_instance():
        if dict_lookup.instance is None:
            with threading.Lock():
                if dict_lookup.instance is None:  # Double locking mechanism
                    dict_lookup()
        return dict_lookup.instance

    def getWords(self): 
        #Getting a list of words from the Github API
        res = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json')
        data = res.json()
        return data


