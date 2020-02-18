from collections import namedtuple
from fastapi import FastAPI
from fastapi.security import OAuth2
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn, requests, json, settings, yt, drive, pprint, pandas as pd

settings.init()
app = FastAPI()
pp = pprint.PrettyPrinter(indent = 4)
origins = [
    "http://localhost",
    "http://localhost:4200",
    "https://localhost",
    "https://localhost:4200",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class rawInput(BaseModel):
    videoId: str
    key: str
    url: str
    feature: str

@app.get("/")
async def read_root():
    return {"Welcome": "Welcome to Youtube API app"}

@app.get("/healthcheck")
async def read_health():
    return {"Welcome": "The Service is ready to receive traffic"}

@app.post("/saveComments")
async def saveComments(input: rawInput, request: Request):
    thread = yt.getCommentThread(input)
    #print(thread)
    #pp.pprint(thread)
    df = pd.DataFrame(thread['items'])
    #print (df)
    df.to_csv('comments.csv')
    drive.uploadFile('comments.csv','text/csv')
    settings.client.service.download('comments.csv', input.videoId)

    return {"Message": "Comments saved and downloaded"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)