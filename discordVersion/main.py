#from botObject import musicbot
import botObject
import discord
#import picklerick
import re

client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith('help buddy'):
        mb = botObject.musicbot('')
        await message.channel.send(mb.helpmessage)
    if message.content.startswith('go buddy'):
        tokens = (message.content).split(' ')
        url = tokens[2]
        mb = botObject.musicbot('Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc')
        platform = mb.findGivenPlatform(url)
        search_creation_object = botObject.search_factory()
        search_object = search_creation_object.create_search(platform)
        meta_data = search_object.search(url)
        result_string = "Artist: " + meta_data['artist'] + '\nAlbum: ' + meta_data['album'] + "\nSong: " + meta_data['song'] 
        await message.channel.send(result_string)
client.run("Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc")



'''

a = botObject.search_factory()
c = a.create_search('open.spotify')
b = c.search('url')
print(b)
'''