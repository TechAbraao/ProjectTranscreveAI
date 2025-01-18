from ...views.insert_url_vw import insert_url_vw
from ...controllers.insert_url_cl import get_title
from ...controllers.insert_url_cl import extract_video_id
from ...controllers.insert_url_cl import download_video

import os

def insert_url_ct():
    os.system("cls||clear")
    value = insert_url_vw()
    
    # Que lógica díficil - Revisar módulo futuramente
    new_value = extract_video_id(value)
    print(get_title(new_value))
    download_video(value)