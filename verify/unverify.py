import discord 
from discord.ext import commands 

from __utils__ import userdb

class Unverify(commands.Cog):
  
  def __init__(self, bot):
    
    self.bot = bot  
    
  @commands.command(aliases = ["logout"]) 
  async def unverify(self, ctx):
    
    user = await userdb.readDB(ctx.author.id)
    
    if user is None:
      
      await ctx.send(":x: | **You currently not verified.**", delete_after = 5)
      
      return
    
    if user[1] != 0: 
      print(user[1])
      success = discord.Embed(description = ":white_check_mark:  **| Succesfully logout.**", color = discord.Colour.green())
      
      success.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
      
      await ctx.send(embed = success)
      
      await userdb.logout(ctx.author.id)
      
      return 
    
    await ctx.reply(":x: | **You currently not verified.**", delete_after = 5)
    
    
    return
  
def setup(bot):
  
  bot.add_cog(Unverify(bot))
