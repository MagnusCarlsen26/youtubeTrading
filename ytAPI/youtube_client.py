import os
from googleapiclient.discovery import build

assert os.environ.get("YT_API_5"), "Please enter Youtube API Key."


def build_youtube_client():

    API_KEY = os.environ.get(f"YT_API_{getYTAPIKey()}")
    return build("youtube", "v3", developerKey=API_KEY)

def getYTAPIKey() : 
    
    # TODO: An algo to get valid API Key
    return 1