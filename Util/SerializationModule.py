#   Author: Joe Ingenito
#   Date Created: 2/25/22
#   Description: Contains methods for serialization in general.

from os import path
import json, pickle

def SerializeJSON(data, filename) :
    """Serialize the data to the specified filename."""
    mode = "w" if path.exists(filename) else "x"
    with open(filename,mode) as json_file:
        json.dump(data,json_file, default=lambda x: x.__dict__)

def DeserializeJSON(filename) :
    """Deserialize an object from the specified filename."""
    with open(filename) as json_file:
        return json.load(json_file)

def PickleData(data,filename) :
    """Use this method to pickle data to the specified filename."""
    mode = "wb" if path.exists(filename) else "xb"
    with open(filename,mode) as f:
        pickle.dump(data,f)

def UnpickleData(filename) :
    """Use this method to unpickle data from the filename."""
    with open(filename,"rb") as f:
        return pickle.load(f)