import os
import re
import threading
import pytubefix
from dotenv import load_dotenv
from googleapiclient.discovery import build
import boto3

load_dotenv()


api_key = os.getenv("YOUTUBE_API_KEY")
if not api_key:
    print("Erro: chave de API não encontrada.")
    exit()


youtube = build("youtube", "v3", developerKey=api_key)


api_key = os.getenv("YOUTUBE_API_KEY")
# print(api_key)

youtube = build("youtube", "v3", developerKey=api_key)


# Função que pega o título atráves da API do Youtube
def get_title(video_id):
    request = youtube.videos().list(
        part = "snippet",
        id = video_id
    )
    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        titulo = response["items"][0]["snippet"]["title"]
        print(f"\n * Título do vídeo: {titulo}")
        return titulo
    else:
        return "Vídeo não encontrado"

# Função que faz a lógica do ID da URL
def extract_video_id(url):
    
    match = re.search(r"(?:v=|\/)([a-zA-Z0-9_-]{11})(?:[&?]|$)", url)
    
    if match:
        return match.group(1)
    else:
        return None  

# Função que baixa vídeo do youtube

def download_video(url):
    yt = pytubefix.YouTube(url, use_po_token=True)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
    
    # onde vai salvar o video
    archive = stream.download(output_path='E:\ProjectTranscreveAi\public\data')
    print("\n * Download concluído.")

    return archive

    # Usando lambda para passar a função correta ao Timer
    # timer = threading.Timer(5, lambda: os.system("cls||clear"))
    # timer.start()

# Função que vai salvar arquivo no S3 - fazer em breve
def set_s3(archive_name):
    aws_key = os.getenv("AWS_ACCESS_KEY")
    aws_secret_key = os.getenv("AWS_ACCESS_SECRET_KEY")
    aws_region = os.getenv("AWS_REGION")
    #name = archive_name
    # print("Verifica " + name) 


    s3 = boto3.client('s3',
                      aws_access_key_id = aws_key,
                      aws_secret_access_key = aws_secret_key,
                      region_name = aws_region 
                      )
    directory = f'{archive_name}'
    bucket_name = 'audiostranscreveai' 
    s3_object_name = f'data/{archive_name}'
    try:
        s3.upload_file(directory, bucket_name, s3_object_name)
        print(f'\n * Arquivo enviado com sucesso para o AWS S3.')
    except Exception as e:
        print(f'\n * Ocorreu um erro: {e}')
    