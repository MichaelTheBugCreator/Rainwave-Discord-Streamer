#Discord bot script to connect to voice chat and play rainwave music from a specific, publicly available mp3
import os
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio as ffmpeg
from dotenv import load_dotenv

#load environment variables. Discord Tokens should not be hard coded in
#The Discord Bot is already iinitialized on discord's side.
#the TOKEN is how we control it specifically.
load_dotenv()
TOKEN = os.getenv('TOKEN_BRAVO')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

#using a hardcoded list of channel ids, automatically join those channels if people entered them,
#and automatically leave if the bot is the last one in the channel
@client.event
async def on_voice_state_update(member, before, after):
    autojoin = [] #list of channel IDs that can be autojoined
    voicelist = [] # will represent the list of channels currently connected to
    for v in client.voice_clients:
        voicelist.append(v.channel.id) #build said list

    #The following comparison works because on_voice_state_update() will fire whenever the voice state of the
    #entire discord server updates. The info included is the specific member whose state updated, what
    #their state was before, and what their state is now (after). Taking the string of after or before
    #returns the name of the channel they were a part of. So, if they changed channel, before should
    #not be the same value as after.
    if str(after) != str(before): #someone joined or left a channel
        if after.channel is not None and after.channel.id in autojoin: #someone joined an autojoin channel
            if after.channel.id not in voicelist: #are we already in it? If not, join in.
                source = "http://allrelays.rainwave.cc/game.mp3"
                channel = after.channel
                vc = await channel.connect()
                audio_source = ffmpeg(source) #turn the mp3 into a streamed audio source that play() can use
                vc.play(audio_source)
        
        if before.channel is not None and before.channel.id in autojoin: #someone left an autojoin channel
            if before.channel.id in voicelist: #are we connected? If yes, check how many members are left.
                channel = client.get_channel(before.channel.id)
                if len(channel.members) == 1: #if we're the only member left, it's time to leave.
                    for v in client.voice_clients:
                        if v.channel.id == channel.id:
                            v.stop()
                            await v.disconnect()

#Actually run the bot, now that we've set up the commands.
client.run(TOKEN)
