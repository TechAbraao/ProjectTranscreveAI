# obtendo titulo através da API do Youtube - Google Cloud

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
        return titulo
    else:
        return "Vídeo não encontrado"
    
def extract_video_id(url):
    video_id = url.split("v=")[-1]
    return video_id
    
video_url = "https://www.youtube.com/watch?v=olDCJ1w3FLM"  
extract = extract_video_id(video_url)
titulo = get_title(extract)
print(f"Título do vídeo: {titulo}")