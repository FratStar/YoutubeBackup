import settings, requests, httpx
from app import rawInput


def getCommentThread(input: rawInput):
    url = settings.ytapi + settings.ytfeatures[1] + 'part=snippet&' + 'maxResults=25&videoId=' + input.videoId + '&key=' + input.key
    response = httpx.get(url).json()
    return response