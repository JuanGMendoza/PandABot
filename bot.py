import asyncio
import discord
from discord.ext import commands, tasks
from random import randint
import tools
import datetime
import os
from dotenv import load_dotenv


intents = discord.Intents().all()
client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():

    #birthday.start()
    print("ready")



@tasks.loop(hours=1)
async def birthday():

    print('here')
    birthday_pandas = tools.check_birthdays()
    # tools.check_birthdays() returns a list with the names whose birthday is today
    # example: ["Kurtony", "Mornet"]
    # check if it's 9am - time to wish a HB
    hour = datetime.datetime.now().hour

    print(birthday_pandas)
    if hour == 16 and len(birthday_pandas) > 0:
        general = tools.get_channel(client, 'bot')

        await general.send("Happy birthday to " + ",".join(birthday_pandas) + "!!" )


load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client.run(token)

