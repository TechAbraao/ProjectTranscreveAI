import yt_dlp

def download_video(url, directory):
    ydl_opts = {
        'format': 'bestaudio/best',  # Baixa o melhor áudio disponível
        'postprocessors': [{  # Converte para MP3 após o download
            'key': 'FFmpegAudio',
            'preferredcodec': 'mp3',  # Define o codec como mp3
            'preferredquality': '192',  # Qualidade do MP3
        }],
        'outtmpl': f'{directory}/%(title)s.%(ext)s',  # Define o formato do arquivo de saída
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

_directory = "E:/Downloads"  # Alterar para o diretório desejado
_url = "https://www.youtube.com/watch?v=hYYXfLdpuds"  # URL do vídeo
download_video(_url, _directory)
