
# youtube-playlist-downloader-as-mp3
A simple script to download entire youtube playlist as Mp3 files.
Made with Python3

**> Not actively maintained <**

**> Legal disclaimer: This application should not be used to download copyrighted material without the copyright holder's consent. This application is intended as an easy way to download the audio of <**

a) your own YT-videos

b) videos you have obtained the permission to download from the copyright holder

c) videos that fall under the public domain or are otherwise free to be used under their license

**> I DO NOT TAKE ANY RESPONSIBILITY, IF YOU DECIDE TO BREAK COPYRIGHT LAW. CIRCUMVENTING COPYRIGHT LAW OR ILLEGALY DOWNLOADING COPYRIGHTED MATERIAL IS A SERIOUS CRIME. PROCEED AT YOUR OWN RISK. <**



# Usage
<ul>
    <li>open cmd and cd to the folder where this script is present</li>
    <li>python youtube_downloader.py --youtube_playlist_link=<youtube_playlist_link> --folder=<path></li>
    <li>Ex., python youtube_downloader.py --youtube_playlist_link=https://www.youtube.com/playlist?list=PL_3ZCwRXK9uicSaLbqRcFrSqdRKzk2z-8 --folder=/Users/shreeharinw/Desktop/custom_songs/audio_only/</li>
    <li>Press Enter and Enjoy!</li>
</ul>


# Requirements
<ul>
    <li>requests (pip install requests)</li>
    <li>pytube (pip install pytube)</li>
    <li>youtube-dl (pip install youtube-dl)</li>
    <li>moviepy (pip install moviepy)</li>
</ul>


# Finally
I want to thank the developers of the amazing pytube package, this powers my script to run efficiently in dowloading entire playlist of a channel.


# How it works?
At its core we are using Pytube to download videos, i wrote this script when downloading playlist was not inbuilt in pytube, so we fetch the list of videos from playlist page and download them in sequence. Then, convert the same to audio and delete the video file.

