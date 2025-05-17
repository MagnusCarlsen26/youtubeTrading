import json
from json import JSONDecodeError

from LLM.geminiAPI import geminiAPI
from ytAPI.getTopSearch import search_top_video
from .json_utils import extract_json_from_string


def extractInfoQuestion( question : str, PROMPT : str ) -> dict  :

    response = geminiAPI( PROMPT.format( question = question ) )
    
    try :

        json_string = extract_json_from_string(response)
        response_data = json.loads( json_string )

        return response_data

    except JSONDecodeError :

        print( "Invalid JSON received from GEMINI" )
        print( f"Attempted to parse : {json_string}" )
        print( f"response from GEMINI : {response}" )

        raise Exception( "Invalid JSON received from GEMINI" )

    except Exception as e:
        
        raise e