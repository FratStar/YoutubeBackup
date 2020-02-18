from __future__ import print_function
import settings, requests, httpx, pickle, os.path
from googleapiclient import discovery
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request




SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.appdata','https://www.googleapis.com/auth/drive.file']
CLIENT_SECRET = './client_secret.json'

creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET, SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

settings.drive_service = discovery.build('drive', 'v3', credentials=creds)


def uploadFile(theFile, mimetype):
    file_metadata = {'name': theFile}
    media = MediaFileUpload(theFile,
                        mimetype=mimetype)

    file = settings.drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    print (f"File ID: {file.get('id')}")
