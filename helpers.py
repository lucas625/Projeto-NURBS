import json

def getJson(jsonPath):
    with open(jsonPath, 'r') as gJson:
        return json.load(gJson)
