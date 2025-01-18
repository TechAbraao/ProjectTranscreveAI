import os
import re
import pytubefix
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


api_key = os.getenv("YOUTUBE_API_KEY")
if not api_key:
    print("Erro: chave de API não encontrada.")
    exit()


youtube = build("youtube", "v3", developerKey=api_key)

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")
# print(api_key)

youtube = build("youtube", "v3", developerKey=api_key)

def get_title(video_id):
    request = youtube.videos().list(
        part = "snippet",
        id = video_id
    )
    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        titulo = response["items"][0]["snippet"]["title"]
        return f"\n * Título do vídeo: {titulo}"
    else:
        return "Vídeo não encontrado"

import re

def extract_video_id(url):
    
    match = re.search(r"(?:v=|\/)([a-zA-Z0-9_-]{11})(?:[&?]|$)", url)
    
    if match:
        return match.group(1)
    else:
        return None  

def download_video(url):
    yt = pytubefix.YouTube(url, use_po_token=True)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
    stream.download(output_path='E:\ProjectTranscreveAi\public\data')