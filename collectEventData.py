from proboAPI.eventInfo import api_eventInfo
from proboAPI.buyBook import api_buyBook

from utils.extractInfoQuestion import extractInfoQuestion
from utils.file_io import writeCSV
from utils.getCurrentDate import getCurrentDate
from utils.time_utils import is_current_time_before_target

from constants import CSV_HEADERS
import time

def collectEventData( eventId : int ) :

    eventInfo = api_eventInfo( eventId )

    targetViews, targetTime, videoId, videoTitle = extractInfoQuestion( eventInfo )

    path = f"data/{getCurrentDate()}/{videoTitle}/{targetTime}"

    writeCSV( f"{path}/yes.csv", CSV_HEADERS )
    writeCSV( f"{path}/no.csv", CSV_HEADERS )

    while is_current_time_before_target( targetTime ) :

        buyBook =  api_buyBook( eventId )
        if buyBook["yesBook"] == {} : return

        currentTime = time.time()

        writeCSV( f"{path}/yes.csv", [ currentTime ] + list( buyBook["yesBook"].values() ) )
        writeCSV( f"{path}/no.csv", [ currentTime ] + list( buyBook["noBook"].values() ) )