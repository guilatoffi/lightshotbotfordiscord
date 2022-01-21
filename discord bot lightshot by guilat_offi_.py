import discord
import random
import string

from discord import message

TOKEN = 'PASTE YOUR TOKEN HERE'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return


    if message.channel.name == 'tchat':
        if user_message.lower() == 'salut':
            await message.channel.send(f'salut {username}!')
            return
        elif user_message.lower() == '!random':
            for i in range(1):
                N = 5
                res = ''.join(random.choices(string.digits + string.ascii_lowercase, k=N))
                response = ("https://prnt.sc/" + str(res))
                await message.channel.send(response)
            return
        elif user_message.lower() == '!random 50':
            for i in range(50):
                N = 5
                res = ''.join(random.choices(string.digits + string.ascii_lowercase, k=N))
                response = ("https://prnt.sc/" + str(res))
                await message.channel.send(response)
            return
        elif user_message.lower() == '!random 10':
            for i in range(10):
                N = 5
                res = ''.join(random.choices(string.digits + string.ascii_lowercase, k=N))
                response = ("https://prnt.sc/" + str(res))
                await message.channel.send(response)
            return
        elif user_message.lower() == '!random 100':
            for i in range(100):
                N = 5
                res = ''.join(random.choices(string.digits + string.ascii_lowercase, k=N))
                response = ("https://prnt.sc/" + str(res))
                await message.channel.send(response)
            return

client.run(TOKEN)

#made by guilat_offi_