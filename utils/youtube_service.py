# https://rapidapi.com/DataFanatic/api/youtube-media-downloader/pricing

import requests
import re
import json


def extract_video_id(url):
    """
    YouTube URL-laridan video ID ajratib beruvchi funksiya.
    """
    patterns = [
        r"v=([a-zA-Z0-9_-]+)",  # Oddiy video
        r"shorts/([a-zA-Z0-9_-]+)",  # YouTube Shorts
        r"embed/([a-zA-Z0-9_-]+)",  # Embed video
        r"youtu\.be/([a-zA-Z0-9_-]+)",  # Youtu.be short link
        r"live/([a-zA-Z0-9_-]+)"  # YouTube Live Stream
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def youtube_down(video_id):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    querystring = {"videoId": video_id}

    headers = {
        "x-rapidapi-key": "9cb3bc16d5msh98edf4f058f8c72p1aad2bjsna26e1f7d4aaa",
        "x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = response.json()
    return result['videos']['items'][0]['url']





# print(youtube_down(video_id="https://www.youtube.com/shorts/pQ_WdAGSHto"))