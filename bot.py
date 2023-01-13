import asyncio
import discord
from discord.ext import commands, tasks
from random import randint
import tools
import datetime
import os
from dotenv import load_dotenv
from discord.utils import get

intents = discord.Intents().all()
client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():

    await birthday.start()
    print("ready")



@tasks.loop(hours=1)
async def birthday():

    birthday_pandas = tools.check_birthdays(client)
    hour = datetime.datetime.now().hour

    if len(birthday_pandas) > 0:
        if "Error" in birthday_pandas[0]:

            dm = await birthday_pandas[1].create_dm()

            await dm.send("Hello! there is an issue with the birthday csv file, please go check it.\n " + birthday_pandas[0])

    

        elif hour == 11:
            general = tools.get_channel(client, 'announcements')

            if len(birthday_pandas) == 1:

                message = "Happy birthday " + birthday_pandas[0] + "! I hope you get to orbit the sun many more times"

            else:

                message = "Today there is an embarrasment of pandas that got older (yes, embarrasment is a group of pandas). Happy birthday to "

                for panda in birthday_pandas:


                    if panda == birthday_pandas[-1]:

                        message += "and " + panda
                    else:

                        message += panda + ", "

                message += "!"

            await general.send(message)


load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client.run(token)

