import discord
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True

#command start with prefix !
bot = Bot(command_prefix="!", intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")
    
@bot.command()    
async def kick_all(ctx):
    await ctx.send('Wait A Second...') # I am alive

    # This is a check for user, if user is you or server owner will be 
    await ctx.send('Started') # Start

    members = ctx.guild.members      # This is list of members
    print(members)
    #members.remove(ctx.me)           # a user can't kick you'r self so remove bot
    #print(members)

    for member in members:           # creating a loop
        print(member.id)
        # Kick



#get your token in the bot page
bot.run('your_token')




