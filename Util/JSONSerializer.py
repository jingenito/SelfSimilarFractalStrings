#   Author: Joe Ingenito
#   Date Created: 2/25/22
#   Description: Contains methods for JSON serialization.

from os import path
import json

def SerializeJSON(data, filename) :
    """Serialize the data to the specified filename."""
    mode = "w" if path.exists(filename) else "x"
    with open(filename,mode) as json_file:
        json.dump(data,json_file, default=lambda x: x.__dict__)

def DeserializeJSON(filename) :
    """Deserialize an object from the specified filename."""
    with open(filename) as json_file:
        return json.load(json_file)