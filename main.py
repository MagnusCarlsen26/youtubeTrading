from proboAPI.eventInfo import api_eventInfo
from utils.extractInfoQuestion import extractInfoQuestion
from ytAPI.getViews import get_video_views

question = api_eventInfo(4030500)
print( extractInfoQuestion(question) )