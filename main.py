from proboAPI.eventInfo import api_eventInfo
from proboAPI.buyEvent import api_buyEvent

from utils.args_parser import parse_trading_args



EVENT_ID, MODE, BUY_QTY = parse_trading_args()

eventInfo = api_eventInfo( EVENT_ID )

# import strategy from strategy/
# decision = strategy( eventInfo )

if decision["isBuy"] :
    
    api_buyEvent( eventId, decision["type"], decision["buyPrice"], qty=BUY_QTY )