import os

from mongoengine import *

from discord.ext import commands

from settings import *

connect('discord', host='localhost', username='root',
        password='root', authentication_source="admin")

bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('OTIwNzcyODE4NDE1ODA0NDM2.YbpOgw.x_a5Drb7eWwtqnzBuuUVyl7BYfk')
