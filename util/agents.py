import pandas as pd
import json
import requests


def loadAgents():
    agentsJson = pd.read_json("data/agents.json")
    return agentsJson

def newAgent(symbol, faction):
    print("New Agent")
    urlFileLocation = "data/requests.json"
    with open(urlFileLocation) as file:
        requestsJson = json.load(file)
        file.close()

    data = {
        "symbol": symbol
        ,"faction": faction
    }

    response = requests.post(requestsJson["Register"], json = data).json()
    token = response['data']['token']
    print(symbol, token)

def getFactionList():

    fileLocation = "data/factions.json"
    with open(fileLocation) as file:
        factionsJson = json.load(file)
        file.close()

    factionsDf = pd.DataFrame.from_dict(factionsJson['data'])
    factionsList = factionsDf['symbol'].to_list()
    return factionsList