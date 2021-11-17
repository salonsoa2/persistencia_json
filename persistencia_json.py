import json

def store(var, filename):
    json.dump(json.dumps(filename), open(filename, "w"))
def retrieve(filename):
    return json.loads(json.load(filename), open(filename, 'r'))