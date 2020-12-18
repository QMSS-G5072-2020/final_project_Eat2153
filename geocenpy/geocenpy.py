import geopandas as gpd
import urllib.request
import json
import base64
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import lxml
import requests

def list_geoparams(**kwargs):
    df_list = pd.read_html('https://github.com/uscensusbureau/citysdk/blob/master/README.md')
    df_params = df_list[2]
    df_table = df_params.replace('✔', 'Yes')
    for k in kwargs:
        year =  kwargs['year']
        if year == '2013' or year == '2014' or year == '2015':
            year = '2013 - 2015'
        elif year == '2016' or year == '2017' or year == '2018' or 'year' == '2019':
            year = '2016 - 2019'
        df_table = df_table[['Geographic Area Type', year]]
    return df_table

def get_geocen_df(quality = "20m", year = "2019", area_type = "state"):
    url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/{quality}/{year}/{area_type}.json"
    df = gpd.read_file(url)
    return df

def get_state_ids(state_initials = str()):
    quality = "20m"
    year = "2019"
    area_type = "state"
    state_initials = state_initials.upper()
    url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/{quality}/{year}/{area_type}.json"
    df = gpd.read_file(url)
    df = df[['NAME', 'STUSPS', 'STATEFP', 'STATENS', 'AFFGEOID', 'GEOID']]
    df = df[df.STUSPS == state_initials]
    return df

def get_geocen_plot(quality = "20m", year = "2010", area_type = "state", boundaries = bool()):
    url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/{quality}/{year}/{area_type}.json"
    df = gpd.read_file(url)
    if boundaries == True:
        return df.boundary.plot()
    else:
        return df.plot()

def get_pop(api_key, year, map = bool()):
    year = year
    pop_url = f'http://api.census.gov/data/{year}/pep/population?get=POP&for=state:*&key={api_key}'
    r = requests.get(pop_url)
    data = json.loads(r.content) 
    pop_df = pd.DataFrame(data[1:], columns=data[0]).\
        rename(columns={"POP": "Pop_Count", "state": "STATEFP"})
    pop_df['Pop_Count'] = pop_df['Pop_Count'].astype(str).astype(int)
    geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/state.json"
    geo_df = gpd.read_file(geodata_url)
    geo_df = geo_df.merge(pop_df, on = 'STATEFP')
    if map == True:
        return geo_df.plot(column = 'Pop_Count')
    else:
        return geo_df

def get_state_house_est(api_key, year, map = bool()):
    year = year
    house_url = f'http://api.census.gov/data/{year}/pep/housing?get=HUEST&for=state:*&key={api_key}'
    r = requests.get(house_url)
    data = json.loads(r.content) 
    house_df = pd.DataFrame(data[1:], columns=data[0]).\
        rename(columns={"HUEST": "Housing_Estimates", "state": "STATEFP"})
    house_df['Housing_Estimates'] = house_df['Housing_Estimates'].astype(str).astype(int)
    geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/state.json"
    geo_df = gpd.read_file(geodata_url)
    geo_df = geo_df.merge(house_df, on = 'STATEFP')
    if map == True:
        return geo_df.plot(column = 'Housing_Estimates')
    else:
        return geo_df

def get_region_pop(api_key, year, map = bool()):
    year = year
    pop_url = f'http://api.census.gov/data/{year}/pep/population?get=POP&for=REGION:*&key={api_key}'
    r = requests.get(pop_url)
    data = json.loads(r.content) 
    pop_df = pd.DataFrame(data[1:], columns=data[0]).\
        rename(columns={"POP": "Pop_Count", "region": "REGIONCE"})
    pop_df['Pop_Count'] = pop_df['Pop_Count'].astype(str).astype(int)
    geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/region.json"
    geo_df = gpd.read_file(geodata_url)
    geo_df = geo_df.merge(pop_df, on = 'REGIONCE')
    if map == True:
        return geo_df.plot(column = 'Pop_Count')
    else:
        return geo_df

def get_state_pop(api_key, year, state_id, map = bool()):
    year = year
    pop_url = f'http://api.census.gov/data/{year}/pep/population?get=POP&for=COUNTY&in=state:*&key={api_key}'
    r = requests.get(pop_url)
    data = json.loads(r.content) 
    pop_df = pd.DataFrame(data[1:], columns=data[0]).\
        rename(columns={"POP": "Pop_Count", "state": "STATEFP"})
    pop_df['Pop_Count'] = pop_df['Pop_Count'].astype(str).astype(int)
    geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/county.json"
    geo_df = gpd.read_file(geodata_url)
    geo_df = ge_df[geo_df.STATEFP == state_initials]
    geo_df = geo_df.merge(pop_df, on = 'STATEFP')

    if map == True:
        return geo_df.plot(column = 'Pop_Count')
    else:
        return geo_df