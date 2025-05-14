import time

from requests import api

from ytAPI.getViews import get_video_views
from utils.time_utils import is_current_time_before_target, get_current_time_ist

def lastMinuteBuyStrat( targetViews : int, targetTime : str, videoId : str ) -> dict :

    apiUsage = 0
    prevViews = None

    t = time.time()
    try :
        while is_current_time_before_target( targetTime ):

            apiUsage += 1
            currentViews = get_video_views( videoId )

            if prevViews is None or prevViews != currentViews : 
                prevViews = currentViews
                print( f"Update {currentViews} at {get_current_time_ist()}" )

            if currentViews > targetViews :

                return {
                    "isBuy" : True,
                    "type" : "yes",
                    "buyPrice" : 9.5,
                }

    except KeyboardInterrupt : 

        duration = time.time() - t
        print( f"API Usage - {apiUsage} in {round( duration/60, 2 ) } mins" )
        print( f"Average call rate - {round( apiUsage/(duration) ,2 )} calls/sec" )

    print(f"Current time is past or equal to target time {targetTime}. Ending strategy.")

    return {
        "isBuy" : False,
    }