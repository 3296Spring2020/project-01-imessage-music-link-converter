import re
import discord
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class musicbot:
    musicPlatformDirectory = {'youtube' : 'Youtube', 'open.spotify' : 'Spotify', 'soundcloud': 'Soundcloud'}
    helpmessage = 'Music Buddy currently supports the following platforms: '
    botToken = None
    def __init__(self, botID):
        self.botToken = botID

    
    def findGivenPlatform(self, URL):
        tokens =  URL.split('/')
        platform = tokens[2]
        platform = re.sub('.com','', platform)
        platform = re.sub('www.','',platform)
        if platform in self.musicPlatformDirectory:
            return self.musicPlatformDirectory[platform] 
        else:
            raiseException("NotSupportedPlatformException")

class search_interface:
    def __init__(self):
        pass
    
    def search():
        pass

    def user_music():
        pass

class release_interface:
    def __init__(self):
        pass
    def search():
        pass
    def release():
        pass

class search_factory:
    def create_search (self, type):
        if type == 'Spotify':
            return spotify_search()
        if type == 'Youtube':
            return  
        else:
            return 'dairy'


            
class spotify_search(search_interface):
    def __init__(self):
        self.client_ID = 'c61123f4ed8945578c7cdb250f75b4b5'
        self.client_secret_key = 'd9f9ffd47a574c9ba9aba01b5662f5d0'
        self.credentials_manager = SpotifyClientCredentials(client_id = self.client_ID, client_secret = self.client_secret_key)
        self.spotify_object =  spotipy.Spotify(client_credentials_manager = self.credentials_manager)
    def search(self, url ):
        # https://open.spotify.com/album/4eLPsYPBmXABThSJ821sqY?highlight=spotify:track:7KXjTSCq5nL1LoYtL7XAwS
        remove_site = re.sub('https://open.spotify.com/album/','', url)
        seperate = re.sub('highlight=spotify:track:','/', remove_site)
        song_ID = seperate.split('/')
        song_ID[0] = song_ID[0][:-1] 
        song = self.spotify_object.track(song_ID[1])
        meta_data = {"artist" : song['artists'][0]['name'] , 'album' :  song['album']['name'] , "song": song['name'] }
        return meta_data2
    def user_music():
        pass

class youtube_search(search_interface):
    def __init__(self):
        pass
    def search():
        return 'youtube'
    def user_music():
        pass