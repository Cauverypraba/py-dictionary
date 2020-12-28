from PyDictionary import PyDictionary
obj = PyDictionary()
obj.create_key('hello')
obj.create_key('xyz')
#obj.create_key(123)
obj.insert('xyz','Hahaaa')
#obj.insert('abc','Hiiii')
print(obj.get('abc'))
#obj.delete('xyz')
