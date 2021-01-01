# PyDictionary

PyDictionary is a python library that acts as a file-based **key-value data store** supporting basic CRD operations. This data store can be instantiated and used as a local storage for single process.

## Installation
1. Download the wheel file from [Latest Release](https://github.com/Cauverypraba/py-dictionary/releases/tag/v1.0). Place it in the project root folder and install using the following command.
```
pip install PyDictionary-1.0-py3-none-any.whl
```
2. Import the library and instantiate data store.
```
from lib.PyDictionary import PyDictionary
...
store = PyDictionary()
...
```

## API
|Method|Arguments|Description|
| --- | --- | --- |
|**create_key**|Key: `string`, TTL_Value: `integer`(optional)|Creates a new key in the store. If TTLValue is given, the key will be alive only for the provided seconds|
|**insert**|Key: `string`, Value: `JSON object`|Inserts given value for the key|
|**delete**|Key: `string`|Removes the given key along with value from the store|
|**get**|Key: `string`|Returns the value of given key|
|**update_ttl**|Key: `string`, TTL_Value: `integer`|Updates the TTL_Value of the given key|

**Note**: ```insert```, ```delete```, ```get``` methods work only when the given key is alive. If the key is timed out, update its Time-To-Live value using ```update_ttl``` method.

## License
This project is licensed under [MIT License](/LICENSE).
