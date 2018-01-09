import discord
import asyncio
from discord.ext import commands

class Anim: 
     def __init__(self, bot):
          self.bot = bot

     @commands.command()
     async def anim(self, ctx):
         c=5
         if c >= 0:
            await ctx.message.edit(content="`THIS MESSAGE WILL SELF DESTRUCT IN %s`" % c)
            await asyncio.sleep(1)
            c -=1
         await ctx.message.edit(content="💣")
         await asyncio.sleep(0.6)
         await ctx.message.edit(content="💥")
       
def setup(bot):
   bot.add_cog(Anim(bot))