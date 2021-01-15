import requests as req
from securetransport import SecureTransport

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

secure = SecureTransport()

channel_url = "https://www.youtube.com/c/RomanMoore"

API_KEY = "AIzaSyASBeMw6E_uKXocqyBBydhzgrzM6Cq9dbQ"
API_KEY_OAUTH = "456132061015-7o7mpikntjujvjfbu7th73hbbkgrjarq.apps.googleusercontent.com"

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

params = {
    'key': API_KEY,
    'part': 'snippet',
    'forUsername': 'RomanMoore',
    'mine': "true"
}
params_new = {
    'key': API_KEY,
    #'id': 'UC_x5XG1OV2P6uZZ5FSM9Ttw',
    'part': 'snippet',
    'mine': 'true'
}

#res = req.get("https://www.googleapis.com/youtube/v3/channels", params=params_new)
#https://developers.google.com/youtube/v3/docs/channels/list?apix_params=%7B%22part%22%3A%5B%22snippet%2CcontentDetails%2Cstatistics%22%5D%2C%22mine%22%3Atrue%7D&apix=true
def main():
    #Disable oauth https verification
    secure.disable()

    api_service_name = 'youtube'
    api_version = 'v3'
    client_secrets_file = 'client_secret_456132061015-'\
                          '7o7mpikntjujvjfbu7th73hbbkgrjarq'\
                          '.apps.googleusercontent.com.json'
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(
        part='snippet',

        mine=True
    )
    response = request.execute()

    print(response)

main()
secure.enable()