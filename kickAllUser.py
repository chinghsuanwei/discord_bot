import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.core import command

#reference from https://stackoverflow.com/questions/68233213/discord-py-kick-all-members-of-server

intents = discord.Intents.default()
intents.members = True

bot = Bot(command_prefix="!", intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")
    
@bot.command()
@commands.has_role("your_role") #TODO specify the role can execute this command
async def kick_all(ctx):
    await ctx.send('Wait A Second...') # I am alive

    # This is a check for user, if user is you or server owner will be 
    await ctx.send('Started') # Start

    members = ctx.guild.members      # This is list of members
    members.remove(ctx.me)           # a user can't kick you'r self so remove bot
       

    for member in members:           # creating a loop
        try:                         # a bot is limited and limit is Error
            print(member.name)
            #TODO
            if member.name != "your_name": # Check member is not you
                # Kick
                await member.kick(reason="See ya!")
                

            else:
                await ctx.send(f"Failed to kick {member}.")
                # This is an log for user.

        except Exception as err: # bot has not permission
            await ctx.send(f"Failed to kick {member}.")
            # This is an log for user.
            continue # Next user

#TODO specify your token
#get your token in the bot page
bot.run('your_token')
