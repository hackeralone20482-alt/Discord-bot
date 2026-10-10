import discord
from discord.ext import commands
​intents = discord.Intents.default()
intents.message_content = True
​bot = commands.Bot(command_prefix='!', intents=intents)
​@bot.event
async def on_ready():
print(f'Logged in as {bot.user.name}')
​@bot.command()
async def hello(ctx):
await ctx.send('Hello there!')
​bot.run('MTU1ODQ4MzgzNDMxMDIzODMzOA.G8mT6y.cSEocAl35DRMHdHWdMjxJgx19B68pfXPPNF5rs')
