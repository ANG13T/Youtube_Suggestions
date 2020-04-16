from youtube_api import YoutubeDataApi

api_key = "AIzaSyBizlTmGnA_2TI-cLQxGSuE7tKXkBvDQRM"
yt = YoutubeDataApi(api_key)



def getStoicData():
    searches = yt.search(q='stoicism', max_results=5)
    searches = [{'title': search['video_title'], 'date': search['video_publish_date'], 'desc': search['video_description'], 'channel': search['channel_title'], 'image': search['video_thumbnail']} for search in searches]
    return searches

def getBusinessData():
    pass
def getMotivationData():
    pass
def getChannelData(channel):
    pass
