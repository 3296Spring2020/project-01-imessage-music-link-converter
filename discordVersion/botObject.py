import re
import discord
class musicbot:

    musicPlatformDirectory = {"youtube" : 0, 'open.spotify' : 1, 'soundcloud': 2}
    id = None
    client = discord.Client() 
    def __init__(self, botID):
        self.id = botID
        #self.client = discord.Client()

    
    @client.event
    async def on_message(message):
        if message.content.startswith('hey buddy'):
            await message.channel.send('Hello!')
    def runBot(self):
        self.client.run(self.id)
    
    @staticmethod
    def findGivenPlatform(URL):
        tokens =  URL.split('/')
        platform = tokens[2]
        platform = re.sub('.com','', platform)
        platform = re.sub('www.','',platform)
        if platform in musicPlatformDirectory:
            return True
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