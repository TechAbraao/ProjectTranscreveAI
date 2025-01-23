import os
from dotenv import load_dotenv
import boto3
load_dotenv()


archive = 'Zion & Lennox ft. Daddy Yankee - Yo Voy (traduçãolegendado).mp4'

def set_s3(archive):
    aws_key = os.getenv("AWS_ACCESS_KEY")
    aws_secret_key = os.getenv("AWS_ACCESS_SECRET_KEY")
    aws_region = os.getenv("AWS_REGION")
    yt = os.getenv("YOUTUBE_API_KEY")
    s3 = boto3.client('s3',
                      aws_access_key_id = aws_key,
                      aws_secret_access_key = aws_secret_key,
                      region_name = aws_region 
                      )
    directory = f'E:/ProjectTranscreveAi/public/data/{archive}'
    bucket_name = 'audiostranscreveai' 
    s3_object_name = f'data/{archive}'
    try:
        s3.upload_file(directory, bucket_name, s3_object_name)
        print(f'Arquivo {archive} enviado com sucesso para {bucket_name}/{s3_object_name}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    

set_s3(archive=archive)