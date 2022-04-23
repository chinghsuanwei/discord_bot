import discord
from discord.ext.commands import Bot

#command start with prefix !
bot = Bot("!")

@bot.command()
async def hello(ctx):
    await ctx.send("Command executed")
    

#get your token in the bot page
bot.run('your_token')



