'''
Python Client Docs
https://github.com/googleapis/google-api-python-client/blob/master/docs

Youtube API Docs
https://developers.google.com/youtube/v3/docs
'''
import os
import json
import googleapiclient.discovery
import googleapiclient.errors
from securetransport import SecureTransport

def get_video_info(youtube, video_ids):
    part_videos = ['snippet', 'statistics']
    #data id : [params]
    data = {}
    count = 0
    while True:
        slice = video_ids[count*50:count*50+50]
        if not slice:
            break
        count += 1
        request = youtube.videos().list(
            part=part_videos,
            id=slice,
            maxResults=50,
        )
        response = request.execute()
        for item in response['items']:
            id = item['id']
            date = item['snippet']['publishedAt']
            if 'tags' in item['snippet']:
               tags = item['snippet']['tags']
            else:
                tags = []
            view = int(item['statistics']['viewCount'])
            like = int(item['statistics']['likeCount'])
            comment = int(item['statistics']['commentCount'])
            dct = {
                'date': date,
                'view': view,
                'like': like,
                'comment': comment,
                'tags': tags
            }
            data[id] = dct
    return data

def get_channel_info(youtube, username):
    request = youtube.channels().list(
        part='id,contentDetails',
        forUsername=username
    )
    response = request.execute()
    channel_id = response['items'][0]['id']
    uploads = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    return channel_id, uploads

def get_video_ids(youtube, uploads):
    next_page_token = ''
    video_id_list = []

    while True:
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response['items']:
            video_id_list.append(item['snippet']['resourceId']['videoId'])
        if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
        else:
            break

    return video_id_list

def get_info(video_path, info_path):
    secure = SecureTransport()
    secure.disable()

    API_KEY = "AIzaSyASBeMw6E_uKXocqyBBydhzgrzM6Cq9dbQ"
    api_service_name = 'youtube'
    api_version = 'v3'
    channel_name = 'MooreDubstep'
    file_name_video_ids = video_path
    file_name_info = info_path
    # Create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    # Create video ids file
    if not os.path.isfile(file_name_video_ids):
        channel_id, uploads = get_channel_info(youtube, channel_name)
        video_id_list = get_video_ids(youtube, uploads)
        with open(file_name_video_ids, 'w', encoding='utf-8') as file:
            json.dump(video_id_list, file, indent=2, ensure_ascii=False)

    with open(file_name_video_ids, 'r') as file:
        video_ids = json.load(file)

    # Create info dict file
    if not os.path.isfile(file_name_info):
        dct = get_video_info(youtube, video_ids)
        with open(file_name_info, 'w') as file:
            json.dump(dct, file, indent=2, ensure_ascii=False)

    with open(file_name_info, 'r') as file:
        dct = json.load(file)

    secure.enable()
