from pytube import YouTube
from pytube.contrib.playlist import Playlist

while True:
    url = input('Please enter a YouTube URL: ')#'https://www.youtube.com/watch?v=ozXb10fOi2A'
    videos = []
    playlist = None

    if not url.startswith('https://youtube.com/watch?v='):
        url = 'https://youtube.com/watch?v=' + url

        videos.append(YouTube(url))
    if url.startswith('https://www.youtube.com/playlist?list='):
        playlist = Playlist(url)

        for video in playlist.video_urls:
            videos.append(YouTube(video))

    if video.streams == []:
        print('Sorry, you can\'t download that video. Try again.')

        continue

    while True:
        quality = input('Please enter quality iTag ("help" for help): ')

        if quality == 'help':
            for stream in video.streams:
                print(stream)
        else:
            try:
                for video in videos:
                    stream = video.streams.get_by_itag(int(quality))

                    if not playlist:
                        stream.download(output_path = "C:\\Users\\manue\\Music\\", filename = input('Please enter a name for the file (Without extension): '))
                    else:
                        stream.download(output_path = "C:\\Users\\manue\\Music\\" + playlist.title, filename = video.title)

                    print("Successfully downloaded!")

                    break   
            except:
                print('iTag must be a number!')