import discord 
from discord.ext import commands 

import os

from __utils__ import userdb

bot = commands.Bot(command_prefix = ">", case_insensitive = True)

@bot.event
async def on_ready():
  await userdb.create_rblx()
  print("Logging in as {}".format(bot.user))
  
cogs = [
  "verify"
  ]  
  
for cog in cogs:
  for filename in os.listdir(f"./{cog}"):
    if filename != "__pycache__" and filename.endswith(".py"):
      bot.load_extension(f"{cog}.{filename[:-3]}")

bot.run(os.environ.get("token")) 
