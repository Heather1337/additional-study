import discord
import secrets
import os
import quote_maker


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Motivation'):
        await message.channel.send(quote_maker.choose_random_quote(quote_maker.quotes))

    elif message.content.startswith('This is hard'):
        await message.channel.send(quote_maker.choose_random_quote(quote_maker.quotes))

    elif message.content.startswith('I am sad'):
        await message.channel.send(quote_maker.choose_random_quote(quote_maker.quotes))
    
    elif message.content.startswith('I am stressed'):
        await message.channel.send(f"Don't worry {message.author}, {quote_maker.choose_random_quote(quote_maker.quotes)}")



# client.run(os.environ['DISCORD_TOKEN'])
client.run("NzYzNjE1NzczNzAwNTIyMDE0.X36Smw.vnK2I9ck_mQh-9ULLKcjZwrRhUY")