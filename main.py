from pytube import YouTube 


def getLink():
    link = input('Enter Youtube link/url: ')
    return link


def downloadMp4(link):
    youtubeObj = YouTube(link)
    videoTitle = youtubeObj.title
    print(f'Title of video: ${videoTitle}')

    if input(f'Are you sure you would like to Download this Youtube video: \n{videoTitle} to MP4? Yes/No  ').lower() == 'yes':
        video = youtubeObj.streams.get_highest_resolution()
        print("Downloading ...")
        try:
            video.download()
        except:
            print('An error occured try again or a different video')
        
        print('Download complete')
    else:
        print('Cancelled. Video will not be Downloaded')



def downloadMp3(link):
    youtubeObj = YouTube(link)
    videoTitle = youtubeObj.title
    print(f'Title of video: ${videoTitle}')

    if input(f'Are you sure you would like to Download this Youtube video: \n{videoTitle} to MP3? Yes/No  ').lower() == 'yes':
        audio = youtubeObj.streams.filter(only_audio=True).first()
        print("Downloading ...")
        try:
            audio.download()
        except:
            print('An error occured try again or a different video')
        
        print('Download complete')
    else:
        print('Cancelled. Video will not be Downloaded')



def main(link):
    userInput = input('Convert Youtube to | MP4 or MP3 |  ')
    videoLink = getLink()
    if userInput.upper() == 'MP4':
        print('You are converting Youtube to MP4 video')
        downloadMp4(videoLink)

    if userInput.upper() == 'MP3':
        print('You are converting Youtube to MP3 audio')
        downloadMp3(videoLink)


if __name__ == '__main__':
    main()