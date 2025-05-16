import os
import random
from googleapiclient.discovery import build

assert os.environ.get("YT_API_1"), "Please enter Youtube API Key."

# TODO: Don't hardcode number of keys
NUMBER_OF_API_KEYS = 1

def build_youtube_client():

    API_KEY = os.environ.get(f"YT_API_{getYTAPIKey()}")
    return build("youtube", "v3", developerKey=API_KEY)

def getYTAPIKey() : 
    
    # TODO: An algo to get valid API Key
    return random.randint( 1,NUMBER_OF_API_KEYS )