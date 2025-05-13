import json
from json import JSONDecodeError

from LLM.geminiAPI import geminiAPI
from ytAPI.getTopSearch import search_top_video
from .json_utils import extract_json_from_string

PROMPT = """
I will give you a sentence please extract the following information :
1. Target Views.
2. Target Time.
3. Video Title.

Output format -
Your resopnse should be in JSON format. JSON Format -  
{{
    targetViews : int,
    targetTime : HH:MM AM/PM,
    videoTitle : str
}}

If you can't find one or more fields then please respond with text ( not json ) about why you can't find the info

Here is the question - {question}
"""

def extractInfoQuestion( question : str ) -> dict  :

    response = geminiAPI( PROMPT.format( question = question ) )
    
    try :

        json_string = extract_json_from_string(response)
        response_data = json.loads( json_string )
        response_data["videoId"] = search_top_video( response_data["videoTitle"] )

        return (
            response_data["targetViews"],
            response_data["targetTime"],
            response_data["videoId"],
            response_data["videoTitle"]
        )

    except JSONDecodeError :

        print( "Invalid JSON received from GEMINI" )
        print( f"Attempted to parse : {json_string}" )
        print( f"response from GEMINI : {response}" )

        raise Exception( "Invalid JSON received from GEMINI" )

    except Exception as e:
        
        raise e