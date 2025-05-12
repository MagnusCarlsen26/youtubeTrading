import json
from json import JSONDecodeError

def extract_json_from_string(response_string: str) -> str:
    # Find the start and end of the JSON object
    json_start = response_string.find('{')
    json_end = response_string.rfind('}')

    if json_start == -1 or json_end == -1:
        print( "Could not find JSON object (missing { or }) in string" )
        print( f"Input string : {response_string}" )
        raise Exception( "Could not find JSON object in string" )

    # Extract the JSON string including the braces and strip surrounding whitespace
    json_string = response_string[json_start : json_end + 1].strip()
    return json_string 