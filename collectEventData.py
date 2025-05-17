from typing import Literal
from proboAPI.eventInfo import api_eventInfo
from proboAPI.buyBook import api_buyBook

from utils.extractInfoQuestion import extractInfoQuestion
from utils.file_io import writeCSV
from utils.getCurrentDate import getCurrentDate
from utils.time_utils import is_current_time_before_target

from constants import CSV_HEADERS, PROMPTS
import time

def collectEventData( eventId : int, EVENT_CATEGORY : Literal["youtube", "bitcoin"] ) :

    eventInfo = api_eventInfo( eventId )

    info = extractInfoQuestion( eventInfo, PROMPTS[ EVENT_CATEGORY ] )

    targetNumber = info["targetNumber"]
    targetTime = info["targetTime"]
    title = info["title"]

    path = f"data/{getCurrentDate()}/{EVENT_CATEGORY}/{title}/{targetTime}-{targetNumber}"

    writeCSV( f"{path}/yes.csv", CSV_HEADERS )
    writeCSV( f"{path}/no.csv", CSV_HEADERS )

    while is_current_time_before_target( targetTime ) :

        buyBook =  api_buyBook( eventId )
        if buyBook["yesBook"] == {} : return

        currentTime = time.time()

        writeCSV( f"{path}/yes.csv", [ currentTime ] + list( buyBook["yesBook"].values() ) )
        writeCSV( f"{path}/no.csv", [ currentTime ] + list( buyBook["noBook"].values() ) )