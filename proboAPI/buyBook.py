import requests

from constants import API_URLS
from utils.sendAPIRequest import sendAPIRequest

def api_buyBook() :

    response = sendAPIRequest( API_URLS["buyBook"].format( eventId=4030500 ), "GET" )

    return {
        "yesBook" : response["available_qty"]["buy"],
        "noBook" : response["available_qty"]["sell"]
    }