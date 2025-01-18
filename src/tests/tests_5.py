import pytubefix


video_url = "https://www.youtube.com/watch?v=ZvRlusdjMSs"

yt = pytubefix.YouTube(video_url, use_po_token=True)


print(f"Título do vídeo: {yt.title}")

stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()


stream.download(output_path='E:\ProjectTranscreveAi\public\data')

print("Download concluído!")