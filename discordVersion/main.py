#from botObject import musicbot
import botObject
import discord
#import picklerick
import re

client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith('help buddy'):
        #pass
        # for key in self.musicPlatformDirectory:
        #     self.helpmessage += self.musicPlatformDirectory[key]
        mb = botObject.musicbot('')
        await message.channel.send(mb.helpmessage)
    if message.content.startswith('go buddy'):
        tokens = (message.content).split(' ')
        url = tokens[2]
        mb = botObject.musicbot('Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc')
        platform = mb.findGivenPlatform(url)
        search_creation_object = botObject.search_factory()
        search_object = search_creation_object.create_search(platform)
        post_search = search_object.search(url)
        await message.channel.send(post_search)
client.run("Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc")



'''

a = botObject.search_factory()
c = a.create_search('open.spotify')
b = c.search('url')
print(b)
'''