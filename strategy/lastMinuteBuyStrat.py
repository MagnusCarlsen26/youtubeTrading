from ytAPI.getViews import get_video_views
from utils.time_utils import is_current_time_before_target, get_current_time_ist

def lastMinuteBuyStrat( targetViews : int, targetTime : str, videoId : str ) -> dict :

    prevViews = None
    while is_current_time_before_target( targetTime ):

        currentViews = get_video_views( videoId )

        if prevViews is None or prevViews != currentViews : 
            prevViews = currentViews
            print( f"Update {currentViews} at {get_current_time_ist()}" )

        if currentViews > targetViews :

            return {
                "isBuy" : True,
                "type" : "yes",
                "buyPrice" : 9.5
            }

    print(f"Current time is past or equal to target time {targetTime}. Ending strategy.")

    return {
        "isBuy" : False,
    }