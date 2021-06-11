import discord
from discord.ext import commands

from __utils__ import userdb
from __utils__ import recog 

class Profile(commands.Cog):
  
  def __init__(self, bot):
    
    self.bot = bot 
    
  @commands.command() 
  async def profile(self, ctx, mentioned: discord.Member = None) -> "Send Profile":
    
    if mentioned is None: 
      mentioned = ctx.author 
      
    readDB = await userdb.readDB(mentioned.id) 
    
    if readDB is None:
      
      await ctx.send(":x: | **You or mentioned are not verified.**")
      return
      
    if readDB[1] == 0:
      
      await ctx.send(":x: | **You or mentioned are not verified.**")
      return 
    
    if readDB[2] == "no":
      
      await ctx.send(":x: | **You or mentioned are not verified.**")
      return
    
    user_name, user_disc, user_id = mentioned.name, mentioned.discriminator, mentioned.id
    
    get_rblx_name = await recog.send_req("notfilled", "get_name", readDB[1])
    user_rblx_id = readDB[1]
    
    proem = discord.Embed(title = f"{ctx.author.name}'s profile.", color = discord.Colour.green())
    
    proem.add_field(name = "Main", value = f"```Name: {user_name}\nDiscriminator: {user_disc}\nID: {user_id}```")
    proem.add_field(name = "Roblox Profile", value = f"```Name: {get_rblx_name}\nRobloxID: {user_rblx_id}```")
    proem.set_footer(text = f"Requested by {ctx.author.name}.", icon_url = ctx.author.avatar_url)
    
    await ctx.send(embed = proem)
    
  @profile.error 
  async def on_profile_err(self, ctx, error):
    
    if isinstance(error, commands.MemberNotFound):
      
      await ctx.send(":x: **| Member not found.**")
      return
  
def setup(bot):
  
  bot.add_cog(Profile(bot))
