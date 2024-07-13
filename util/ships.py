import pandas as pd
import json
import requests
import util.sqlite_functions as sqf
import streamlit as st
import util.nav as nav

class Ship():
    def __init__(self, shipDic):
        self.symbol = shipDic['symbol']
        self.registration = shipDic['registration']
        self.nav = shipDic['nav']
        self.crew = shipDic['crew']
        self.frame = shipDic['frame']
        self.reactor = shipDic['reactor']
        self.engine = shipDic['engine']
        self.cooldown = shipDic['cooldown']
        self.modules = shipDic['modules']
        self.mounts = shipDic['mounts']
        self.cargo = shipDic['cargo']
        self.fuel = shipDic['fuel']

    def get_ships_for_charting(self, token):
        waypoint = nav.get_waypoint(token, self.nav['systemSymbol'], self.nav['waypointSymbol'])
        #print(waypoint)
        shipDic = {
            "symbol" : self.symbol
            ,"systemSymbol" : self.nav['systemSymbol']
            ,"type" : "Ship"
            , "x": waypoint['data']['x']
            , "y": waypoint['data']['y']
            , "waypoints": self.nav['waypointSymbol']
            , "factions" : waypoint['data']['faction']['symbol']
        }
        return shipDic

def find_shipyards(token, system):
    data = nav.search_system(token, system, "SHIPYARD")
    if data['data']: 
        return data['data']
