import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = 'bot', intents = intents)
#it is @client.event bcuz in the previous line the word client is used. If it was poo = commands.Bot....... then it would be poo.event
@client.event
async def on_ready():
    print("Ohayo")
#again client is used in client.run bcuz it was declared as client = commands.bot....

@client.event
async def on_member_join(member):
    print('w-w-welcome to the server'f'{member}, y-you joining doesnt make us happy or anything >///<') #f in this statement acts as a variable and must be used


client.run('Nzg0MTEzODEwMTg1MTI1OTIw.X8kk5A.OslqRzf6Hw6f6RoE6GTfr_0WDoM')
