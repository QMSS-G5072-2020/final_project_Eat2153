from geocenpy import __version__
from geocenpy import geocenpy
import geopandas as gpd
import urllib.request
import json
import base64
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import lxml
import requests
from requests.exceptions import HTTPError

def test_version():
    assert __version__ == '0.1.0'

def test_list_geoparams():
    geoparams_df = geocenpy.list_geoparams()
    assert type(geoparams_df) == pandas.core.frame.DataFrame

def test_get_geocen_df():
    df = geocenpy.get_geocen_df(quality = "20m", year = "2010", area_type= "county")
    assert df.shape == (3221, 7)

def test_get_state_ids():
    geoID = geocenpy.get_state_ids(state_initials = "OR")
    assert type(geoID) == pandas.core.frame.DataFrame