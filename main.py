import requests as req
import os
from securetransport import SecureTransport

secure = SecureTransport()
secure.disable()

channel_url = "https://www.youtube.com/c/RomanMoore"

API_KEY = "AIzaSyASBeMw6E_uKXocqyBBydhzgrzM6Cq9dbQ"
API_KEY_OAUTH = "456132061015-7o7mpikntjujvjfbu7th73hbbkgrjarq.apps.googleusercontent.com"

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

res = req.get("https://www.googleapis.com/youtube/v3/channels", params=params_new)
#https://developers.google.com/youtube/v3/docs/channels/list?apix_params=%7B%22part%22%3A%5B%22snippet%2CcontentDetails%2Cstatistics%22%5D%2C%22mine%22%3Atrue%7D&apix=true
def main():
    pass

secure.enable()