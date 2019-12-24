from __future__ import unicode_literals
import webbrowser
import os
import shutil
import datetime
from bs4 import BeautifulSoup
import urllib.request
import youtube_dl
dirpath = os.path.dirname(os.path.realpath(__file__))
now = datetime.datetime.now()
print('Today is ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' and the time is ' + str(now.hour) + ':' + str(now.minute))
# For those that are given in square brackets '[]' just type the letter inside to continue or the whole command (the word)
Answer = input('[s]ong or [p]laylist? ')
if Answer == 'song' or Answer == 's':
    # This is for playing a single song
    Song = input('What is the song? ')
    try:
        os.startfile(dirpath + '\Py' + '\\' + Song + '.mp3')
    except:
        print('lol')
elif Answer == 'playlist' or Answer == 'p':
    relevancy = input('[O]ld, [n]ew, [e]dit playlist or [d]ownload a song? ')
    if relevancy == 'edit' or relevancy == 'e':
        # This one is to edit old playlists, the whole program is jumbled in orders (I think this part has a few problems)
        play = input('Which playlist would you like to edit? ')
        playlist = open(dirpath + '\\Playlists\\' + play + '.txt', "r+")
        edited = []
        print('This are the current songs in ' + play + ':')
        for line in playlist:
            print(line)
            edited.append(line)
        for old in playlist:
            print(old)
        print('What would you like to add to ' + play + '? ')
        newsong = 'none'
        while newsong != 'done':
            newsong = input('Add this to ' + play + ' ')
            edited.append(newsong + '\n')
        edited.remove('done\n')
        for old in playlist:
            print(old)
        print('What would you like to delete from ' + play + '? ')
        newsong = 'none'
        while newsong != 'done':
            newsong = input('Delete this song from ' + play +' ')
            if newsong == 'done':
                edited.append('done')
                edited.remove('done')
            else:
                edited.remove(newsong + '\n')
        playlist.close()
        os.remove(dirpath + '\\Playlists\\' + play + '.txt')
        playlist = open(dirpath + '\\Playlists\\' + play + '.txt', "w+")
        for new in edited:
            playlist.write(new)
        print(play + ' has been edited')
        print('The current playlist has these songs:')
        print(edited)
        playlist.close()
    if relevancy == 'old' or relevancy == 'o':
        # This opens an old playlist that you created
        file = open(dirpath + '\Playlists' + '\\' + input('Name the playlist ') + '.txt', "r+")
        for wav in file:
            mp3 = []
            for letter in wav:
                mp3.append(letter)
            mp3.pop(-1)
            wav = ''
            for item in mp3:
                wav = wav + item
            os.startfile(dirpath + '\Py' + '\\' + wav + '.mp3')
        file.close()
    if relevancy == 'new' or relevancy == 'n':
        # This created a new playlist, you need to enter each of the songs, then the playlist is played
        Song = 'nothing'
        playlist = []
        while Song != 'done':
            Song = input('Add this song to playlist ')
            playlist.append(Song)
        playlist.remove('done')
        playd = []
        for tune in playlist:
            try:
                os.startfile(dirpath + '\Py' + '\\' + tune + '.mp3')
                playd.append(tune)
            except:
                print('...')
        Creator = input('Wanna save this playlist? (yes/no)')
        if Creator == 'yes':
            Creator = input('Name the playlist ')
            if os.path.isfile(dirpath + '\\Playlists\\' + Creator + '.txt') == True:
                while os.path.isdir(dirpath + '\\Playlists\\' + Creator + '.txt') == True:
                    Creator = input('Nah man this playlist is taken. Choose another one ')
                file = open(dirpath + '\\Playlists\\' + Creator + '.txt', "w+")
                for mp in playd:
                    file.write( mp + '\n')
                    print(mp + ' has been added to the playlist')
                print('Congratulations the new playlist ' + Creator + ' has been created')
            else:
                file = open(dirpath + '\\Playlists\\' + Creator + '.txt', "w+")
                for mp in playd:
                    file.write( mp + '\n')
                    print(mp + ' has been added to the playlist')
                print('Congratulations the new playlist ' + Creator + ' has been created')
            file.close()
        else:
            print('Welp')
    if relevancy == 'download' or relevancy == 'd':
        # This is the download section, you enter the query in YouTube and select which one you want
        text  = input('What do you want to search? ')
        query = urllib.parse.quote(text)
        url = 'https://www.youtube.com/results?search_query=' + query
        respone = urllib.request.urlopen(url)
        html = respone.read()
        soup = BeautifulSoup(html, 'html.parser')
        allvid = soup.findAll(attrs={'class':'yt-uix-tile-link'}, limit=10)
        vid = allvid[0]
        print('Here are the results:')
        print(vid['title'])
        print('https://www.youtube.com' + vid['href'])
        ask = input('Is this the video? (yes/no)')
        x = 1
        if ask == 'yes':
            name = input('What would you like to name it? ')
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': True,
            'outtmpl': dirpath + '\Py' + '\\' + name + '.%(ext)s'
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com' + vid['href']])
        elif ask ==  'no':
            while input('Is this the video? (yes/no)') == 'no':
                vid = allvid[x]
                print(vid['title'])
                print('https://www.youtube.com' + vid['href'])
            name = input('What would you like to name this? ')            
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'

            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': True,
            'outtmpl': dirpath + '\Py' + '\\' + name + '.%(ext)s'
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com' + vid['href']])
        os.remove(dirpath + '\Py\\' + name + '.webm')
        print('It has been downloaded')
    print('bye!')
else:
    print('There is no such command K Thx Bye!')