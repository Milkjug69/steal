#imports
import config
import discord
from discord import mentions
from discord.ext.commands import Bot
from discord import Intents
import random
import string

intents = discord.Intents(messages=True)
client = discord.Client(intents)
bot = Bot(command_prefix='$',intents=intents)
#token
token = config.token
status={'snooping'}
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(status)))
string.ascii_letters
@bot.event
async def on_message(message):
    if message.author.bot:
        await bot.process_commands(message)
        return
    if message.content == '!commands':
        await message.channel.send('try; !help, !add,!website')
        await bot.process_commands(message)
        # print("commands")
    if message.content == '!url':
        user = 1
        for i in range(user):
            x = random.choice(string.ascii_letters)
            y = random.choice(string.ascii_letters)
            a = random.randrange(0, 9)
            b = random.randrange(0, 9)
            c = random.randrange(0, 9)
            d = random.randrange(0, 9)
            f = ("https://prnt.sc/" + str(x.lower() + y.lower()) + str(int(a, )) + str(int(b)) + str(int(c)) + str(
                int(d)))
        await message.channel.send(f)
        await bot.process_commands(message)
        # print("commands")


bot.run(token)


