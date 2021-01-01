import json
import time
import sys
import uuid
import os
from threading import Lock

class PyDictionary:
    def __init__(self):
        # Generating Unique file name for each instance
        self.file_name = 'data-store-' + str(uuid.uuid1())
        # Write Initial value to file
        self.write_file({})
        self.lock = Lock()
        self.ttlMap = {}
    
    def create_key(self, key, ttlValue=0):
        '''Creating a unique key in JSON file and checking the conditions
        for the key'''
        self.lock.acquire()
        data = self.read_file()
        # Checks the size of file in GB    
        file_size = sys.getsizeof(data)
        size_in_gb = file_size / 1000000000
        if(size_in_gb > 1):
            raise Exception("File size should be less than 1GB")
        # Checks the conditions for keys
        if key in data:
            raise Exception("Key '" + key + "' already exists, please provide Unique key")
        if type(key) != str:
            raise TypeError("Key '"+ key +"' must be a string")
        if len(key) > 32:
            raise ValueError("Length of key should not be more than 32")
        data[key] = None
        self.write_file(data)
        self.ttlMap[key] = {
            'time': time.time(),
            'ttl': ttlValue
        }
        self.lock.release()


    def insert(self, key, value):
        ''' Inserting value to the key only when size of value is less than 16KB'''
        self.lock.acquire()
        # Insert values to the specified keys
        data = self.read_file()
        size_in_bytes = sys.getsizeof(value)
        size_in_kb = size_in_bytes / 1024
        if key not in data:
            raise Exception("Key '" + key + "' does not exist")
        # Checks whether key is alive
        if not self.__is_key_alive(key):
            raise Exception("Key '" + key + "' is not alive, please update Time-To-Live value")
        # Checks the size of value in kilobytes
        if size_in_kb > 16:
            raise ValueError("Size of value should not be greater than 16 KB")
        data[key] = value
        self.write_file(data)
        self.lock.release()

    def delete(self, key):
        '''Delete the key that exists'''
        self.lock.acquire()
        data = self.read_file()
        if key not in data:
            raise Exception("Key '" + key + "' does not exist")
        # Checks whether key is alive
        if not self.__is_key_alive(key):
            raise Exception("Key '" + key + "' is not alive, please update Time-To-Live value")
        del data[key]
        self.write_file(data)
        self.lock.release()

    def get(self, key):
        '''read operation performed and recieved a value
        in response'''
        self.lock.acquire()
        data = self.read_file()
        if key not in data:
            raise Exception("Key '" + key + "' does not exist")
        # Check whether key is alive
        if not self.__is_key_alive(key):
            raise Exception("Key '" + key + "' is not alive, please update Time-To-Live value")
        self.lock.release()
        return data[key]
       
    def __is_key_alive(self, key):
        ''' Returns whether Key is Alive'''
        now = time.time()
        ttlObj = self.ttlMap[key]
        if (ttlObj['ttl'] == 0) or (ttlObj['time'] + ttlObj['ttl'] > now):
            return True
        else:
            return False

    def update_ttl(self, key, ttlValue):
        ''' Updates Time To Live Value of given key  '''
        self.lock.acquire()
        if key not in self.ttlMap:
            raise Exception("Key '" + key + "' does not exist")
        self.ttlMap[key]['time'] = time.time()
        self.ttlMap[key]['ttl'] = ttlValue
        self.lock.release()

    def read_file(self):
        ''' Opens the JSON file and returns the json object as a dictionary '''
        with open(self.file_name + '.json') as file:
            data = json.load(file)
        return data

    def write_file(self, data):
        ''' Writes given dictionary into JSON file '''
        with open(self.file_name + '.json', 'w') as file:
            json.dump(data, file)

    def __del__(self):
        # Delete JSON file when instance is destroyed
        os.remove(self.file_name + '.json')
        