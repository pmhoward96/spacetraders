import pandas as pd
import json
import requests
import streamlit
import util.sqlite_functions as sqf

dbFile = "spacetraders\data\spaceTradersDb.db"
#sqf.create_connection("spacetraders\data\spaceTradersDb.db")

agentColumns = [["Symbol", "VARCHAR(50) NOT NULL"], ["Token", "VARCHAR(255) NOT NULL"]]

#sqf.create_table("spacetraders\data\spaceTradersDb.db", "Agents", agentColumns, "Symbol")

dataDict = {"Symbol" : ["Prey", "Prey2"], "Token": ["asdfasdf", "asdfasdf"]}

agentDf = pd.DataFrame(dataDict)
print(agentDf)
sqf.insert_data(dbFile, "Agents", agentDf)