import os
import json
import datetime as DT
import matplotlib.pyplot as plt

import ytbscrapper


video_path = r'C:\Users\d.abramov\PycharmProjects' \
             r'\WebScrappingYoutube\video_ids.json'
info_path = r'C:\Users\d.abramov\PycharmProjects' \
            r'\WebScrappingYoutube\video_info.json'

if not os.path.isfile(video_path) or not os.path.isfile(info_path):
    ytbscrapper.get_info(video_path, info_path)

with open(info_path, 'r') as file:
    info = json.load(file)

dates = []
for key in info:
    dates.append(DT.datetime.strptime(info[key]['date'], "%Y-%m-%dT%H:%M:%SZ"))
print(dates)
