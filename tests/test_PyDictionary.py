from threading import Thread
import time
import unittest
from lib.PyDictionary import PyDictionary

class TestDictionary(unittest.TestCase):

    def test_duplicate_key(self):
        ''' Raises an exception when we try to create a key that already exists'''
        d = PyDictionary()
        d.create_key('name')
        with self.assertRaises(Exception):
            d.create_key('name')         

    def test_invalid_key(self):
        ''' Checks whether key is a string'''
        d = PyDictionary()
        with self.assertRaises(TypeError):
            d.create_key(10)

    def test_long_key(self):
        ''' Checks size of the key if it is greater than 32 there will be an exception'''
        d = PyDictionary()
        with self.assertRaises(ValueError):
            d.create_key('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    
    def test_keyin_dict(self):
        ''' Checks key exists in the dictionary to insert value for specified key'''
        d = PyDictionary()
        with self.assertRaises(Exception):
            d.insert('hii','haii')

    def test_key_timeout(self):
        ''' Checks whether the key is alive to insert value to the key specified'''
        d = PyDictionary()
        d.create_key('name', 3)
        time.sleep(5)
        with self.assertRaises(Exception):
            d.insert('name', 'max')

    def test_keyin_dict(self):
        ''' Checks key exists in the dictionary to delete key'''
        d = PyDictionary()
        with self.assertRaises(Exception):
            d.delete('hii','haii')

    def test_key_timeout(self):
        ''' Checks whether the key is alive to delete a key specified'''
        d = PyDictionary()
        d.create_key('name', 3)
        time.sleep(5)
        with self.assertRaises(Exception):
            d.delete('name', 'max')     

    def test_keyin_dict(self):
        ''' Checks key exists in the dictionary to read the value of a key'''
        d = PyDictionary()
        with self.assertRaises(Exception):
            d.get('hii','haii')

    def test_key_timeout(self):
        ''' Checks whether the key is alive to read a key'''
        d = PyDictionary()
        d.create_key('name', 3)
        time.sleep(5)
        with self.assertRaises(Exception):
            d.get('none')           

    def test_keyin_dict(self):
        ''' Checks key exists in the dictionary only then Time-To-Live for a key will get updated'''
        d = PyDictionary()
        with self.assertRaises(Exception):
            d.updateTTL('hii', 10)        