from proboAPI.getAllEvents import api_getAllEvents

from constants import TOPIC_IDS

from collectEventData import collectEventData

import threading

runningEvents = []

def main() :

    events = api_getAllEvents( TOPIC_IDS["youtube"] )
    
    for event in events:

        eventId = event["id"]

        if eventId not in runningEvents :
            runningEvents.append( eventId )
            print(f"Tasks : {runningEvents}")

    for eventId in runningEvents:
        thread = threading.Thread(target=processEventInThread, args=(eventId,))
        thread.start()

def processEventInThread(eventId):
    collectEventData(eventId)

if __name__ == "__main__":
    main()