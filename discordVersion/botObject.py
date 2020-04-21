import re
import discord
import spotipy
import deezer
from spotipy.oauth2 import SpotifyClientCredentials

class musicbot:
    music_platform_directory = {'youtube' : 'Youtube', 'open.spotify' : 'Spotify', 'soundcloud': 'Soundcloud', 'deezer' : 'Deezer'}
    help_message = 'Music Buddy currently supports the following platforms: Spotify, Deezer'
    bot_token = None
    
    def __init__(self, botID):
        self.bot_token = botID

    
    def find_given_platform(self, URL):
        tokens =  URL.split('/')
        platform = tokens[2]
        platform = re.sub('.com','', platform)
        platform = re.sub('www.','',platform)
        if platform in self.music_platform_directory:
            return self.music_platform_directory[platform] 
        else:
            raiseException("find_given_platform() ---> Not Supported Platform Exception")

    def find_target_platform (self, user_input):
        tokens = user_input.split(' ')
        target = tokens[3]
        if target in self.music_platform_directory:
            return self.music_platform_directory[target]
        else:
            raiseException("find_target_platform() ---> Not Supported Platform Exception")

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
        if type == 'Deezer':
            return  deezer_search()
        else:
            raiseException("create_search() ----> Unable to Create Search Object")


            
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
        meta_data = {"artist" : song['artists'][0]['name'] , 'album' :  song['album']['name'] , "song": song['name'] , "release" : song['album']['release_date'] }
        return meta_data
    def user_music():
        pass

class deezer_search(search_interface):
    def __init__(self):
        self.app_ID = '408302'
        self.secret_key = '625152fbf950ee7b70ee61fb6988aab2'
        self.client = deezer.Client(app_id= self.app_ID , app_secret = self.secret_key)
        
    def search():
        return 'youtube'
    def user_music(self, meta_data):
        query = self.client.search(meta_data['song'])
        url = query[0].link
        return ap3