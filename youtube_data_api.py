from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import json

#ALL LIKED VIDEOS FROM MY YOUTUBE CHANNEL

CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()

#api_key='<api_key>'

youtube = build('youtube', 'v3', credentials=credentials)

request = youtube.playlistItems().list(
    playlistId='LLlY4Roho4V3-gunrDEifPsA',
    part='snippet',
    maxResults=50
)
response = request.execute()

for item in response['items']:
    print(item['snippet']['title'])


#print(json.dumps(response, indent=4, sort_keys=True))


