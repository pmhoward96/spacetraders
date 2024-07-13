import pandas as pd
import json
import requests
import util.sqlite_functions as sqf
import streamlit as st
import plotly.express as px
import util.ships as ships


waypoint_types = ["PLANET", "GAS_GIANT", "MOON", "ORBITAL_STATION", "JUMP_GATE", "ASTEROID_FIELD", "ASTEROID", "ENGINEERED_ASTEROID", "ASTEROID_BASE", "NEBULA", "DEBRIS_FIELD", "GRAVITY_WELL", "ARTIFICIAL_GRAVITY_WELL", "FUEL_STATION"]

def chart_entire_universe_with_selections(ships = None):
    df = sqf.get_all_values("Systems")
    print("Ships to Chart", ships)
    if ships is not None:
        shipsDf = pd.DataFrame(ships)
        df = pd.concat([df, shipsDf])
    print("Charting", df)
    fig = chart_system(df)
    event = st.plotly_chart(fig, key = "galaxyFig", on_select = "rerun")
    #print(event)
    if len(event['selection']['points']) > 0:
        systemList = []
        for s in event['selection']['points']:
             systemList.append(s['customdata'][0])
        
        return systemList
    else:
         return ""


def chart_system(df):
    fig = px.scatter(
        df
        ,x = 'x'
        , y= "y"
        ,color = 'type'
        ,symbol = 'type'
        ,hover_data=['symbol']
    )

    return fig

def search_system(token, system, traits=None):
    if traits == None:
        url = "https://api.spacetraders.io/v2/systems/" + system + "/waypoints"
    else:
         url = "https://api.spacetraders.io/v2/systems/" + system + "/waypoints?traits=" + traits
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()
    else:
            print(f"Error: {response.status_code} - {response.text}")

def get_all_waypoints(token, page):
    url = "https://api.spacetraders.io/v2/systems?limit=20&page=" + page 
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()
    else:
            print(f"Error: {response.status_code} - {response.text}")

def get_waypoint(token, systemSymbol, waypointSymbol):
    url = f"https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints/{waypointSymbol}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()
    else:
            print(f"Error: {response.status_code} - {response.text}")
