from youtube_api import YoutubeDataApi
from secret import youtube_api

yt = YoutubeDataApi(youtube_api)



def getVideoData(search):
    searches = yt.search(q=search, max_results=10)
    print(searches[0])
    searches = [{'title': search['video_title'], 'date': search['video_publish_date'], 'desc': search['video_description'], 'channel': search['channel_title'], 'image': search['video_thumbnail'],  'video_link': "https://www.youtube.com/watch?v=" + search['video_id']} for search in searches]
    return searches

def getChannelData(channel):
    pass

