'''
Python Client Docs
https://github.com/googleapis/google-api-python-client/blob/master/docs

Youtube API Docs
https://developers.google.com/youtube/v3/docs
'''
from securetransport import SecureTransport

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

secure = SecureTransport()
secure.disable()

API_KEY = "AIzaSyASBeMw6E_uKXocqyBBydhzgrzM6Cq9dbQ"
api_service_name = 'youtube'
api_version = 'v3'

part_list_channel = ['brandingSettings', 'contentDetails',
        'contentOwnerDetails', 'id', 'localizations', 'snippet',
        'statistics', 'status', 'topicDetails']

part_list_playlist = ['contentDetails', 'id', 'localizations',
                      'player', 'snippet', 'status']

part_list_playlistitems = ['contentDetails', 'id', 'snippet',
                           'status']

#Create an API client
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)
request = youtube.channels().list(
        part='id,contentDetails',
        forUsername='MooreDubstep'
    )
response = request.execute()
print(response)
CHANNEL_ID = response['items'][0]['id']
UPLOADS = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


counter = 0
next_page_token = ''

while True:
    request = youtube.playlistItems().list(
        part=','.join(part_list_playlistitems),
        playlistId=UPLOADS,
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()
    print(response)
    if 'nextPageToken' in  response:
        next_page_token = response['nextPageToken']
    else:
        break
    for item in response['items']:
        #print(item['snippet']['resourceId']['videoId'])
        counter += 1
        print(counter)


secure.enable()