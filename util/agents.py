import pandas as pd
import json
import requests
import util.sqlite_functions as sqf
import util.contracts as contracts
import util.ships as ships
import streamlit as st


class Agent():
    def __init__(self, agentDic):
        self.token = agentDic["token"][0]
        self.symbol = agentDic["symbol"][0]
    
    def get_agent_token(self):
        return self.token

    def get_agent_info(self):
        url = "https://api.spacetraders.io/v2/my/agent"
        headers = {'Authorization': f'Bearer {self.token}'}
        print(headers)
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    def get_contracts(self):
        url = "https://api.spacetraders.io/v2/my/contracts"
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            contractList = []
            for c in response.json()["data"]:
                contractList.append(contracts.Contract(c))
                return contractList
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    def get_ships(self):
        url = "https://api.spacetraders.io/v2/my/ships"
        headers = headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            shipList = []
            for c in response.json()["data"]:
                print(c['symbol'])
                shipList.append(ships.Ship(c))
            return shipList
        else:
            print(f"Error: {response.status_code} - {response.text}")
    

def load_all_agents():
    df = sqf.get_all_values("Agents")
    return df

