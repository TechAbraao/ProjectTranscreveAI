# Verificando se tá retornando o titulo ou não. Teste totalmente fracassado kkkkk

import yt_dlp
import warnings

def get_tittle_url(_value_insert_url):
    ydl_opts = {
        'quiet': True,  
        'force_generic_extractor': True 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(_value_insert_url, download=False)
        video_title = info_dict.get('title', None)
        print(video_title)

warnings.filterwarnings("ignore", message=".*ffmpeg not found.*")
value_insert_url = str(input("Insert value: "))
get_tittle_url(value_insert_url)