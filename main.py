import argparse

from proboAPI.eventInfo import api_eventInfo
from utils.extractInfoQuestion import extractInfoQuestion
from ytAPI.getViews import get_video_views
from strategy.lastMinuteBuyStrat import lastMinuteBuyStrat

parser = argparse.ArgumentParser(description="Run trading script with specified event ID and mode.")
parser.add_argument("--eventId", type=int, help="The event ID for the trading operation.")
parser.add_argument("--mode", type=str, choices=['dev', 'prod'], help="The mode for the trading operation (can be 'dev' or 'prod').")
parser.add_argument("--buyQty", type=int, help="The quantity to buy. Required in 'prod' mode.")

args = parser.parse_args()

if args.mode == "prod" and args.BUY_QTY is None:
    parser.error("BUY_QTY is required when mode is 'prod'.")

EVENT_ID = args.eventId
MODE = args.mode

if MODE == "dev" :
    BUY_QTY = 1
elif MODE == "prod":
    BUY_QTY = args.buyQty

eventInfo = api_eventInfo( EVENT_ID )

# This has : targetViews, targetTime, videoId
targetTime, targetViews, videoId, videoTitle = extractInfoQuestion( eventInfo )

print( f"Question - {videoTitle}, {targetTime}, {targetViews}" )

lastMinuteBuyStrat( targetTime, targetViews, videoId )