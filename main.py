import pandas as pd
import json
import requests
import streamlit as st
import sys
import util.agents as agents
import util.contracts as contracts
import util.nav as nav
import util.ships as ships
import util.streamlit_util as stu
import sqlite3

st.set_page_config(
    page_title="SpaceTraders",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Space Traders")

###################################################
#Streamlit Session State Keys 
agentKey = "agent"
if agentKey not in st.session_state:
    st.session_state[agentKey] = ""


with st.sidebar:
    st.title("Select Agent")

    #Get agents
    agentsDf = agents.load_all_agents()
    agentsList = agentsDf.symbol
    agentSymbol = st.selectbox("Select Agent", agentsList)
    if st.button("Load Agent"):
        st.session_state[agentKey] = agents.Agent(agentsDf[agentsDf["symbol"] == agentSymbol].to_dict())

st.header("Ships")
shipsList = st.session_state[agentKey].get_ships()
#print(shipsList)
st.dataframe(stu.custom_object_list_to_df(shipsList))

print("Ships Listing")
chartShipList = []
for s in shipsList:
    tempS = s.get_ships_for_charting(st.session_state[agentKey].get_agent_token())
    chartShipList.append(tempS)
    

st.header("Contracts")
st.dataframe(stu.custom_object_list_to_df(st.session_state[agentKey].get_contracts()))

systemSelection = nav.chart_entire_universe_with_selections(chartShipList)

##print(systemSelection)
shipyards = []
for s in systemSelection:
    shipyards.append(ships.find_shipyards(st.session_state[agentKey].get_agent_token(), s))

shipyards = list(filter(lambda item: item is not None, shipyards))
print(shipyards)