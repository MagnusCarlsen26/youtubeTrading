from utils.sendAPIRequest import sendAPIRequest
from constants import API_URLS

def api_getAllEvents( topicId : int ) :

    response = sendAPIRequest( 
        API_URLS["getAllEvents"], 
        "POST",
        headers={
            "x-device-os": "ANDROID",
            "x-version-name": "10",
        },
        payload={
            "filter" : {},
            "limit" : 15,
            "page" : 1,
            "sortType" : "",
            "topicIds" : [ topicId ]
        }
    )

    return response["records"]["events"]