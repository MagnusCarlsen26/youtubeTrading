from proboAPI.getAllEvents import api_getAllEvents

from constants import TOPIC_IDS

from collectEventData import collectEventData

import threading

runningEvents = []


def main( MAGIC_KEY : bool ) :

    if not MAGIC_KEY : return 

    events = api_getAllEvents( TOPIC_IDS["youtube"] )
    
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
    
    collectEventData( eventId )
    main( MAGIC_KEY )

if __name__ == "__main__":
    main( MAGIC_KEY = True )