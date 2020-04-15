import re
import discord
import picklerick
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
    def inp (self, type):
        if type == 'open.spotify':
            return spotify_search()
        if type == 'youtube':
            return  


            
class spotify_search(search_interface):
    def __init__(self):
        pass
    def search(self):
        return 'spotify'
    def user_music():
        pass

class youtube_search(search_interface):
    def __init__(self):
        pass
    def search():
        return 'youtube'
    def user_music():
        pass