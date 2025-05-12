from constants import API_URLS
from utils.sendAPIRequest import sendAPIRequest

def api_eventInfo( eventId : int ) :

    response = sendAPIRequest( API_URLS["eventInfo"].format( eventId = eventId), "GET" )

    return response["name"]