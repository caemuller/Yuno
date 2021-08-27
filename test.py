import discord as disc
import os

client = disc.Client()

#online message
@client.event
async def on_ready():
    print('{0.user} is online <3'.format(client))

#message form the bot
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('//y hi'):
        await message.channel.send("Hi I'm Yuno")
    
client.run(os.getenv('yuno_code'))