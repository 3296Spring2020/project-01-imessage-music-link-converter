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

class searchInterface:
    def __init__(self):
        pass
    
    def searchForMeta():
        pass

    def userMusic():
        pass

class releaseInterface:
    def __init__(self):
        pass
    def search():
        pass
    def finalpush():
        pass