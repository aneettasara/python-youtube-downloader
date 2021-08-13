# import pytube module
from pytube import YouTube

# download path
download_path = "youtube-downloader/youtube-videos"

# URL of the video to be downloaded from Youtube
link = "https://www.youtube.com/watch?v=k1Pu0_tIgR4"

try:
    # object creation using pytube
    yt = YouTube(link)
except: 
    # handle exception
    print("Connection Error at Youtube!!")

# details of the Youtube video
print("Title of video: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)

# set streams settings
video = yt.streams.filter(file_extension="mp4").first()

try:
    # downloading the video 
    print("Downloading...") 
    video.download(download_path)
    print("Download completed!!")
except:
    # handle exception
    print("Unable to download. Try again!!")  

# Youtube video is downloaded
print("\nTask Completed!")

'''
sample output
-------------
Title of video:  Dear Women by Women Who Code
Number of views:  18588
Length of video:  110
Downloading...
Download completed!!

Task Completed!
'''