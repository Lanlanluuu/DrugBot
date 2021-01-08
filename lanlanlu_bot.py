#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
from DrugBot import runLoki as drugbot

DISCORD_TOKEN="Nzg5Mzc1MDAzMDE5NDQ0MjY0.X9xIwg._C3Ym9ltsmYlFV2TTBatTZnqe5k"
DISCORD_GUILD="Droidtown Linguistics Tech."
BOT_NAME = "DrugBot"

# Documention
# https://discordpy.readthedocs.io/en/latest/api.html#client

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break
    print(f'{BOT_NAME}bot has connected to Discord!')
    print(f'{guild.name}(id:{guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("message.content", message.content)
    if "<@!{}>".format(client.user.id) in message.content: # (client.user.id) is botID
        if "haiyya" in message.content:
            response = "Help!"
            await message.channel.send(response)
            
        elif 'test' in message.content:
            response = "Sleeping zZzZ"
            await message.channel.send(response)
        elif "你在幹嘛" in message.content:
            response = "https://tenor.com/view/pedro-monkey-puppet-meme-awkward-gif-15268759"
            await message.channel.send(response)
        
        else:
            response = drugbot([message.content])
            await message.channel.send(response)
        
    elif "bot 點名" in message.content:
        response = "又 (˙w˙)"
        await message.channel.send(response)
    
    else:
        pass


client.run(DISCORD_TOKEN)