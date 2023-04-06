from pytube import YouTube 




def downloadMp4(link):
    youtubeObj = YouTube(link)
    video = youtubeObj.streams.get_highest_resolution()


    return video.download()