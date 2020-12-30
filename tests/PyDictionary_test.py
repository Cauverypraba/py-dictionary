from threading import Thread
import time
from lib.PyDictionary import PyDictionary
obj = PyDictionary()
obj.create_key('hello', 5)
obj.create_key('xyz')

#obj.create_key('xyz')
#obj.create_key(123)
obj.insert('hello','Hahaaa')
obj.insert('xyz', 'hhhh')
#obj.insert('abc','Hiiii')

time.sleep(7)
obj.updateTTL('hello', 5)
print(obj.get('hello'))
print(obj.get('xyz'))
#obj.delete('xyz')

# print(obj.create_key('hi'))
# t1 = Thread(target=obj.create_key, args=("hai",))
# t2 = Thread(target=obj.create_key, args=("hai",))
# t1.start()
# t2.start()

# t1.join()
# t2.join()