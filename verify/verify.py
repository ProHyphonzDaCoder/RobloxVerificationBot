import discord
from discord.ext import commands 

import aiohttp 
import aiosqlite
import asyncio

from __utils__ import userdb
from __utils__ import recog
from __utils__ import captcha

class Verify(commands.Cog):
  
  def __init__(self, bot):
    
    self.bot = bot 
    
  @commands.command() 
  @commands.cooldown(1, 10.0, commands.BucketType.user)
  async def verify(self, ctx, name = None):
    
    user = await userdb.readDB(ctx.author.id)
    
    if user is None or user[1] == 0:
      
      if name is None: return await ctx.send(":x: **| Specify Roblox user.**")
      
      recogs = await recog.send_req(name, "not", 0)
      
      try: 
        
        rblx_id = int(recogs) 
        
        cptc = await captcha.get_captcha() 
        
        cfrm = discord.Embed(title = "Profile", description = f"Usernames: {name}\nID: {rblx_id}\n\n**Is this your profile? respond with Y/n.**", color = discord.Colour.green())
        
        await ctx.send(embed = cfrm)
        
        try: 
          
          confirmasi = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 60.0)
          
        except asyncio.TimeoutError:
          
          await ctx.send(":x: | Timeout Error.")
          return 
        
        else:
          
          if confirmasi.content.lower() in ["yes", "ya", "y"]:
            
            await ctx.send(f":white_check_mark: | **Change your Roblox Profile Description to this following captcha**:\n```{cptc}```\n\n**If done, execute this command again.**")
            
            await userdb.verify(ctx.author.id, rblx_id, "no", cptc) if user is None else await userdb.update_status(ctx.author.id, rblx_id, "no", cptc)
            
            return
          
          elif confirmasi.content.lower() in ["no", "n"]: 
            
            await ctx.send(":x: | **cancelled.**", delete_after = 10)
            
            return
        
        
      except ValueError:
        print("error")
        await ctx.send(recogs)
        return
    
    else:
      
      if user[2] == "no":
        
        bio = await recog.send_req("notfilled", "after_code", user[1])
        
        if bio == user[3]: 
          
          success = discord.Embed(title = "Success", description= ":white_check_mark: **| You succesfully verified!**", color = discord.Colour.green())
          
          await ctx.send(embed = success)
          
          await userdb.update_verify_status(ctx.author.id, user[1], "yes")
          
        else: 
          
          await ctx.send(f":x: | Captcha wrong.\nYour captcha: ```{user[3]}```")
          return
      
      else: 
        
        await ctx.send(f":x: | You already registered as **{user[1]}**")
        
  @verify.error 
  async def on_verify_error(self, ctx, error):
    
    if isinstance(error, commands.CommandOnCooldown):
      
      await ctx.send(f":x: | **Command on cooldown. try after {round(error.retry_after)} seconds.**") 
      
      return

def setup(bot):
  
  bot.add_cog(Verify(bot))
  
