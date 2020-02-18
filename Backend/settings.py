from zeep import Client

client = Client(wsdl='http://localhost:8001/?wsdl')

def init():
    global ytapi
    global driveapi
    global ytfeatures
    global drivefeatures
    global drive_service
    ytapi = 'https://www.googleapis.com/youtube/v3/'
    driveapi = 'https://www.googleapis.com/upload/drive/v3/'
    ytfeatures = ['search?', 'commentThreads?']
    drivefeatures = ['files?']
