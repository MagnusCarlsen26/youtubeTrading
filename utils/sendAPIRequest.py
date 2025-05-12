import os
import requests
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

assert os.environ.get("PROBO_BEARER_TOKEN"), "Please enter Auth Token"
AUTH_TOKEN = os.environ.get("PROBO_BEARER_TOKEN")

def sendAPIRequest( url : str, method : Literal["GET","POST","PUT"], headers={} ) :

    headers["authorization"] = AUTH_TOKEN

    if method == "GET" : response = requests.get( url=url, headers=headers )
    elif method == "POST" : response = requests.post( url=url, headers=headers )
    elif method == "PUT" : response = requests.put( url=url, headers=headers )

    if response.status_code != 200 : 
        raise Exception( f"Error from Probo : {response.json()["message"]}" ) 
    else :

        response = response.json()

        if response["isError"] : 
            raise Exception( f"Error from Probo : {response["message"]}" )

        return response["data"]