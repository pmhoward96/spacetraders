import pandas as pd
import json
import requests
import streamlit as st
import sys
import util.agents as agents
import util.streamlit_util as stu
import sqlite3

print(st.session_state)

urlFileLocation = "data/requests.json"
with open(urlFileLocation) as file:
    requestsJson = json.load(file)
    file.close()

st.title("Space Traders")

with st.sidebar:
    st.title("Select Agent")

    registerData = {
        "symbol": "Prey_test"
        , "faction": "COSMIC"
    }
    #Get agents
    agentsDf = agents.loadAgents()
    st.selectbox("Select Agent", agentsDf)
    
    if "registerAgentButton" not in st.session_state:
        st.session_state["registerAgentButton"] = False
    if "submitAgentRegisterButton" not in st.session_state:
        st.session_state["submitAgentRegisterButton"] = False

    if st.button("Register New Agent"):
        if not st.session_state["registerAgentButton"]:
            with st.form("New Agent"):
                newAgent = st.text_input("Agent Name to Register")
                factionList = agents.getFactionList()
                faction = st.selectbox("Select Faction", factionList)
                submitted = st.form_submit_button("Submit")
                if submitted:
                    print("submitted")
                    response = agents.newAgent(newAgent, faction)
        stu.sessionStateCallback("registerAgentButton")                
    #print(dir(registerResponse))
       # if 'error' in registerResponse.keys():
           # print("Agent has already been registered", registerResponse['error']['data']['agentSymbol'])
        #else:
           # print(registerResponse['data'])

