import discord
import asyncio
import time
import sys

from bot import Bot

token = open('token.txt',"r").read().strip()

client = discord.Client()

@client.event
async def on_read():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!channels'):
        await client.send_message(message.channel,client.get_all_channels())

    print(str(message.channel)+": "+message.content)

if(__name__=="__main__"):
    print("Bot Started")
    client.run(token)
