import discord
from discord.ext import tasks
from pymongo import MongoClient
import asyncio
import datetime
import schedule
import time
import logging

clientdb = MongoClient('mongodb://localhost:27017/') # Change the URL to your MongoDB URL
db = clientdb['db2'] # Change the database name to your database name
collection = db['db2'] # Change the collection name to your collection name
client_id = 111 # Change the client ID to your client ID, This is the channel where the bot will send the news
TOKEN = '' # GIVE YOUR DISCORD BOT TOKEN HERE

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)


async def send_news():
    print("sending news")
    while True:
        items = collection.find({'isPosted': False, 'isValid': True}).sort('time', 1)

        channel = client.get_channel(client_id)
        for item in items:
            try:
                url = item['url']
                print("url: " + url)
                embed = discord.Embed(title=item['title'], url=url,
                                      description="Click the title or the url down below to read more!", color=0x1a5dda)
                embed.add_field(name="Publish Date", value=item['time'].strftime('%Y-%m-%d'))
                embed.set_author(name="Scam News", url=url)
                embed.set_footer(text="News provided by [scamalert.sg]")
                await channel.send(embed=embed)
                await channel.send(url)
                await channel.send("————————————————————————————————————————————————————————————")
                collection.update_one({'_id': item['_id']}, {'$set': {'isPosted': True}})
            except discord.errors.HTTPException as e:
                collection.update_one({'_id': item['_id']}, {'$set': {'isValid': False}})
                print(f"Invalid URL in item: {item}. Skipping.")
                continue

        print("finished sending news")
        await asyncio.sleep(600)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await send_news()


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(TOKEN, log_handler=handler, root_logger=True)
