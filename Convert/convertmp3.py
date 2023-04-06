from pytube import YouTube 




def downloadMp3(link):
    youtubeObj = YouTube(link)
    videoTitle = youtubeObj.title
    audio = youtubeObj.streams.filter(only_audio=True).first()


    return audio.download()
     




