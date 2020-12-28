import json
import sys

class PyDictionary:
    def __init__(self):
        file = open("data-store.json", "w+")
        ''' Write Initial value to file '''
        json.dump({}, file)

    # def create_key(self, key):
    #     '''check key is string with size 32 chars
    #     value should be JSON object with size 16KB.
    #     check create is not invoked for existing key
    #     else return error'''
    #     with open('data-store.json') as file:
    #         data = json.load(file)
    #     if key not in data:
    #         data[key] = None
    #         if type(key) == str:
    #             if len(key) <= 32:
    #                 with open('data-store.json', 'w') as file:
    #                     json.dump(data, file)
    #             else:
    #                 print("Key size should not be more than 32")
    #         else:
    #             print("Key must be string")
    #     else:
    #         print("Key already exists")
    #
    #     ''''''

    def create_key(self, key):
        '''opening the JSON file and reads the json object into
        a dictionary'''
        with open('data-store.json') as file:
            data = json.load(file)
        '''Checking the conditions for keys'''
        if key in data:
            raise Exception("Key already exists")
        if type(key) != str:
            raise TypeError("Key must be string")
        if len(key) > 32:
            raise ValueError("Key size should not be more than 32")
        data[key] = None
        with open('data-store.json', 'w') as file:
            json.dump(data, file)


    def insert(self, key, value):
        '''insert values to the specified keys'''
        with open('data-store.json') as file:
            data = json.load(file)
        size_in_bytes = sys.getsizeof(value)
        size_in_kb = size_in_bytes / 1024
        if key not in data:
            raise Exception("Key does not exist")
        '''check the size of value in kilobytes'''
        if size_in_kb > 16:
            raise ValueError("Size of value should not be greater than 16")
        data[key] = value
        with open('data-store.json', 'w') as file:
            json.dump(data, file)

    def delete(self, key):
        with open('data-store.json') as file:
            data = json.load(file)
        if key not in data:
            raise Exception("Key does not exist")
        del data[key]
        with open('data-store.json', 'w') as file:
             json.dump(data, file)

    def get(self, key):
        '''read operation performed and recieved a value
        in response'''
        with open('data-store.json') as file:
            data = json.load(file)
        if key not in data:
            raise Exception("Key does not exist")
        with open('data-store.json', 'w') as file:
             json.dump(data, file)
        return data[key]