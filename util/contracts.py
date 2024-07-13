import pandas as pd
import json
import requests
import util.sqlite_functions as sqf
import streamlit as st

class Contract():
    def __init__(self, contractDic):
        self.id = contractDic["id"]
        self.factionSymbol = contractDic["factionSymbol"]
        self.type = contractDic["type"]
        self.terms = contractDic["terms"]
        self.accepted = contractDic["accepted"]
        self.fulfilled = contractDic["fulfilled"]
        self.expiration = contractDic["expiration"]
        self.deadlineToAccept = contractDic["deadlineToAccept"]

    def print_contract(self):
        print(self.id)
        print(self.factionSymbol) 
        print(self.type) 
        print(self.terms) 
        print(self.accepted) 
        print(self.fulfilled)  
        print(self.expiration)  
        print(self.deadlineToAccept)
    
    def accept_contract(self, token):
        url = "https://api.spacetraders.io/v2/my/contracts/" + self.id + "/accept'"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            self.accepted = True
            return True
        else:
            print(f"Error: {response.status_code} - {response.text}")

