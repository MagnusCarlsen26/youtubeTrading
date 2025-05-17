import threading
from typing import Literal

from proboAPI.getAllEvents import api_getAllEvents

from constants import TOPIC_IDS

from collectEventData import collectEventData


from utils.args_parser import parse_trading_args

runningEvents = []

def main( MAGIC_KEY : bool, EVENT_CATEGORY : Literal["youtube", "bitcoin"] ) :


    if not MAGIC_KEY : return 

    events = api_getAllEvents( TOPIC_IDS[ EVENT_CATEGORY ] )
    
    for event in events:

        eventId = event["id"]

        if eventId not in runningEvents :
            runningEvents.append( eventId )
            print(f"Tasks : {runningEvents}")

    for i, eventId in enumerate( runningEvents ) :

        magicKeyForThread = MAGIC_KEY if i == 0 else False
        
        thread = threading.Thread( target = processEventInThread, args=( eventId, magicKeyForThread, ) )
        thread.start()

def processEventInThread( eventId : int, MAGIC_KEY : bool ):
    
    collectEventData( eventId, EVENT_CATEGORY )
    main( MAGIC_KEY, EVENT_CATEGORY )

if __name__ == "__main__":
    EVENT_CATEGORY = parse_trading_args()
    main( MAGIC_KEY = True, EVENT_CATEGORY = EVENT_CATEGORY )