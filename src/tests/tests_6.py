import boto3
import os
import time
from dotenv import load_dotenv
load_dotenv()

aws_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_ACCESS_SECRET_KEY")
aws_region = os.getenv("AWS_REGION")
# print(f"\n1 - {aws_key}\n2 - {aws_secret_key}\n3 - {aws_region}")

session = boto3.Session(
    aws_access_key_id=aws_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)
client_transcribe = session.client("transcribe")

# ----
bucket_name = "audiostranscreveai"
file_name = "data/audio_1.mp3"
job_name = "exemplo-teste-02"

response = client_transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    LanguageCode='pt-BR',  # ou 'en-US', dependendo do idioma
    Media={'MediaFileUri': f's3://{bucket_name}/{file_name}'},  # URI do arquivo no S3
    MediaFormat='mp3',  # ou 'mp4', 'wav', etc. conforme o formato do seu arquivo
    OutputBucketName=bucket_name  # Bucket onde o resultado será armazenado
)
while True:
    status_response = client_transcribe.get_transcription_job(TranscriptionJobName=job_name)
    status = status_response['TranscriptionJob']['TranscriptionJobStatus']
    
    print(f'Job Status: {status}')
    
    if status in ['COMPLETED', 'FAILED']:
        break
    
    print("Aguardando...")
    time.sleep(30)  # Aguarda 30 segundos para verificar o status novamente

# Se a transcrição for concluída, exibe o link do arquivo JSON com a transcrição
if status == 'COMPLETED':
    transcript_url = status_response['TranscriptionJob']['Transcript']['TranscriptFileUri']
    print(f'A transcrição foi concluída! Acesse o arquivo JSON em: {transcript_url}')
else:
    print('A transcrição falhou.')

print(transcript_url)