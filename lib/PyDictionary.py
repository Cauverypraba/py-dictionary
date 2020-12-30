import json
import time
import sys
from threading import Lock

class PyDictionary:
    def __init__(self):
        file = open("data-store.json", "w+")
        ''' Write Initial value to file '''
        json.dump({}, file)
        self.lock = Lock()
        self.ttlMap = {}


    def create_key(self, key, ttlValue=0):
        '''Creating a unique key in JSON file and checking the conditions
        for the key'''
        self.lock.acquire()
        #opening the JSON file and reads the json object into a dictionary
        with open('data-store.json') as file:
            data = json.load(file)
        #checking the size of file in GB    
        file_size = sys.getsizeof(data)
        size_in_gb = file_size / 1000000000
        if(size_in_gb > 1):
            raise Exception("File size should be less than 1GB")
        print(file_size, size_in_gb)
        #Checking the conditions for keys
        if key in data:
            raise Exception("Key '" + key + "' already exists, please provide Unique key")
        if type(key) != str:
            raise TypeError("Key must be a string")
        if len(key) > 32:
            raise ValueError("Length of key should not be more than 32")
        data[key] = None
        with open('data-store.json', 'w') as file:
            json.dump(data, file)
        self.ttlMap[key] = {
            'time': time.time(),
            'ttl': ttlValue
        }
        self.lock.release()


    def insert(self, key, value):
        ''' Inserting value to the key only when size of value is less than 16KB'''
        self.lock.acquire()
        #insert values to the specified keys
        with open('data-store.json') as file:
            data = json.load(file)
        size_in_bytes = sys.getsizeof(value)
        size_in_kb = size_in_bytes / 1024
        if key not in data:
            raise Exception("Key does not exist")
        # Checking whether key is alive
        if not self.__isKeyAlive(key):
            raise Exception("Key is not alive, please create again")
        # Check the size of value in kilobytes
        if size_in_kb > 16:
            raise ValueError("Size of value should not be greater than 16")
        data[key] = value
        with open('data-store.json', 'w') as file:
            json.dump(data, file)
        self.lock.release()

    def delete(self, key):
        '''Delete the key that exists'''
        self.lock.acquire()
        with open('data-store.json') as file:
            data = json.load(file)
        if key not in data:
            raise Exception("Key does not exist")
        # Checking whether key is alive
        if not self.__isKeyAlive(key):
            raise Exception("Key is not alive, please create again")
        del data[key]
        with open('data-store.json', 'w') as file:
            json.dump(data, file)
        self.lock.release()

    def get(self, key):
        '''read operation performed and recieved a value
        in response'''
        self.lock.acquire()
        with open('data-store.json') as file:
            data = json.load(file)
        if key not in data:
            raise Exception("Key does not exist")
        # Checking whether key is alive
        if not self.__isKeyAlive(key):
            raise Exception("Key is not alive, please create again")
        self.lock.release()
        return data[key]
       
    def __isKeyAlive(self, key):
        ''' Returns whether Key is Alive'''
        now = time.time()
        ttlObj = self.ttlMap[key]
        print(ttlObj)
        if (ttlObj['ttl'] == 0) or (ttlObj['time'] + ttlObj['ttl'] > now):
            return True
        else:
            return False

    def updateTTL(self, key, ttlValue):
        ''' Updates Time To Live Value of given key  '''
        self.lock.acquire()
        if key not in self.ttlMap:
            raise Exception("Key does not exist")
        self.ttlMap[key]['time'] = time.time()
        self.ttlMap[key]['ttl'] = ttlValue
        self.lock.release()