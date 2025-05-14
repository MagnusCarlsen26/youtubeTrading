from proboAPI.eventInfo import api_eventInfo
from proboAPI.buyEvent import api_buyEvent

from utils.extractInfoQuestion import extractInfoQuestion
from utils.args_parser import parse_trading_args

from strategy.lastMinuteBuyStrat import lastMinuteBuyStrat


EVENT_ID, MODE, BUY_QTY = parse_trading_args()

eventInfo = api_eventInfo( EVENT_ID )

# This has : targetViews, targetTime, videoId
targetTime, targetViews, videoId, videoTitle = extractInfoQuestion( eventInfo )

print( f"Question - {videoTitle}, {targetTime}, {targetViews}" )

decision = lastMinuteBuyStrat( targetTime, targetViews, videoId )

if decision["isBuy"] :
    
    api_buyEvent( eventId, decision["type"], decision["buyPrice"], qty=BUY_QTY )