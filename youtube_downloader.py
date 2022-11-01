from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
import sys
import argparse

parser = argparse.ArgumentParser(
        description="Script to download the youtube playlist as mp3 files.")
parser.add_argument("--youtube_playlist_link", required=True,
                    help="Enter the youtube playlist link. Example: https://www.youtube.com/playlist?list=PL_3ZCwRXK9uicSaLbqRcFrSqdRKzk2z-8")
parser.add_argument("--folder", required=True,
                    help="Folder in which the files to be downloaded. Example: /Users/shreeharinw/Desktop/custom_songs/audio_only")
args = parser.parse_args()

youtube_playlist_link = args.youtube_playlist_link
folder = args.folder
# Ex., 
# folder = "/Users/shreeharinw/Desktop/custom_songs/video_songs"
# playlist = Playlist("https://www.youtube.com/playlist?list=PL_3ZCwRXK9uicSaLbqRcFrSqdRKzk2z-8")
playlist = Playlist(youtube_playlist_link)


#prints each video url, which is the same as iterating through playlist.video_urls
for url in playlist:
    print(url)
#prints address of each YouTube object in the playlist
for vid in playlist.videos:
    print(vid)

# YouTube(url).streams.filter(only_audio=True).first().download('/Users/shreeharinw/Desktop/custom_songs/video_songs')
for url in playlist:
   YouTube(url).streams.filter(only_audio=True).first().download(folder)

for file in os.listdir(folder):
  if re.search('mp4', file):
    mp4_path = os.path.join(folder,file)
    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)