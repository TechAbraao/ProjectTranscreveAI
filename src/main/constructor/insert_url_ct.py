from ...views.insert_url_vw import insert_url_vw
from ...controllers.insert_url_cl import get_title
from ...controllers.insert_url_cl import extract_video_id
from ...controllers.insert_url_cl import download_video
from ...controllers.insert_url_cl import set_s3

import os

def insert_url_ct():
    os.system("cls||clear")
    value = insert_url_vw()
    
    # Que lógica díficil - Revisar módulo futuramente
    new_value = extract_video_id(value)
    title = get_title(new_value)
    video = download_video(value)
    # print(title)
    set_s3(video)