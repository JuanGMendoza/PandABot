# helper functions used by the bot
from discord import ChannelType
import os
from random import randint
import datetime

# Returns true if the date is within a month in the past/future of the current date.
# Returns false otherwise
def valid_date(dateToCheck):

    today = datetime.date.today()

    dateToCheck = datetime.date(
        int(dateToCheck[-2:]) + 2000, int(dateToCheck[:2]), int(dateToCheck[3:-3])
    )

    difference = today - dateToCheck

    if int(difference.days) > 30:
        return False

    else:
        return True

# returns the voice channel the user is connected to
# returns None if user is not in any voice channel
def find_voice_channel(user, client):

    for channel in client.get_all_channels():
        if channel.type == ChannelType.voice:

            for member in channel.members:

                if member == user:
                    return channel

    return None


def check_birthdays():
    today = datetime.date.today()
    birthday_pandas = []

    data = open("birthdays.csv", "r")

    for line in data:

        print(line)
        name, birthday = line.split(",")

        if name == 'Name':
            continue


        month, day = birthday.split("-")

        if today.month == int(month) and today.day == int(day):
            birthday_pandas.append(name)

    data.close()

    return birthday_pandas


def get_channel(bot, name):

    channels = bot.guilds[0].text_channels

    for channel in channels:

        if name in channel.name:
            return channel

