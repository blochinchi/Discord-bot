import discord  #imported the library of discord.py
import random
import asyncio


from discord.ext import commands    #from the discord extension, we've imported the commands library
intents = discord.Intents.all()
pip = commands.Bot(command_prefix = ['pip ', 'pop '], intents=intents)    #we've set 'pip' as the prefix, the bot OwO uses owo as its prefix and mudae uses '$'

#class discord.Embed(title = "title")

#it is @pip.event bcuz in the previous line the word pip is used. If it was poo = commands.Bot....... then it would be poo.event


@pip.event      #creates the event function. An event is a piece of code that runs when the bot detects a certain activity has happened.
async def on_ready():   #async stands for asynchronous function. on_ready runs the code below it, when the bot comes online in the terminal. It runs it only once at the beginning
    print("BANZAI") #print only sends a message in the terminal and not on discord.

@pip.event
async def on_member_join(member):   #runs the code below when a member joins.
    channel = pip.get_channel(847552325286363199) #it specifies a certain channel. It has been hardcoded to "737933993340698664" here. This is not advised when dealing with a lot of servers as it could break if that channel does not exist.
    await channel.send("w-w-welcome to the server"f"{member.mention}, y-you joining doesnt make us happy or anything >///<")
    print("welcome") #f in this statement acts as a variable and must be used

@pip.command() #creates the command function. A command is a piece of code that is executed when the user tells the bot to do something.
async def name(ctx):
    await ctx.send("idk your name "f"{ctx.author.name}")

@pip.command()
async def id(ctx, user: discord.User):
    await ctx.send(user.name)

@pip.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(pip.latency*1000)} ms")

@pip.command()
async def gif(ctx):
    await ctx.send("hello")


@pip.command()
async def pat(ctx, user: discord.User):
    responses=["https://tenor.com/view/anime-pat-smile-cute-blush-gif-16456868",
               "https://tenor.com/view/misha-misha-necron-anos-voldigoad-the-misfit-of-demon-king-academy-headpat-pat-gif-18243417",
               "https://tenor.com/view/kanna-kamui-pat-head-pat-gif-12018819",
               "https://tenor.com/view/anime-pet-gif-9200932",
               "https://tenor.com/view/patpat-pat-comfort-patonthehead-therethere-gif-10534102",
               "https://tenor.com/view/pat-cute-kawaii-anime-asterisk-gif-13792462",
               "https://tenor.com/view/anime-smile-head-pat-bed-gif-16243971",
               "https://tenor.com/view/rascal-does-not-dream-of-bunny-girl-senpai-seishun-buta-yar%c5%8d-anime-head-pat-rest-gif-17747839",
               "https://tenor.com/view/charlotte-pat-blush-embarrassed-shy-gif-5081286",
               "https://tenor.com/view/charlotte-pat-blush-embarrassed-shy-gif-5081286",
               "https://tenor.com/view/head-pat-anime-kawaii-neko-nyaruko-gif-15735895",
               "https://tenor.com/view/anime-pat-smile-cute-blush-gif-16456868",
               "https://tenor.com/view/kyo-ani-musaigen-phantomworld-izumi-anime-gif-4977531",
               "https://tenor.com/view/anime-head-rub-head-pat-pat-rub-gif-16085328",
               "https://tenor.com/view/nogamenolife-shiro-headrub-sleepy-tired-gif-6238142",
               "https://tenor.com/view/rikka-head-pat-pat-on-head-anime-rikka-gif-13911345",
               "https://cdn.weeb.sh/images/BJp1lyYD-.gif",
               "https://cdn.weeb.sh/images/HkZqkyFvZ.gif",
               "https://tenor.com/view/anime-head-pat-heat-pat-head-massage-gif-12434286"]
    await ctx.send(f"{ctx.author.name} pats "f"{user.name}\n"f"{random.choice(responses)}")

@pip.command()
async def punch(ctx):
    responses=["https://tenor.com/view/tgggg-anime-punch-gif-13142581",
               "https://tenor.com/view/naruto-sasuke-punch-snicker-anime-gif-7380310",
               "https://tenor.com/view/anime-punch-knockout-wasted-smack-gif-11451829",
               "https://tenor.com/view/anime-punch-angry-slam-wall-gif-5012021",
               "https://tenor.com/view/bear-fight-hit-teddy-bear-kids-gif-12373244",
               "https://tenor.com/view/punch-anime-punch-you-in-the-face-gif-5357324",
               "https://tenor.com/view/mimi-cute-anime-tap-gif-15633073",
               "https://tenor.com/view/punch-anime-fight-angry-attack-gif-16634439"]
    await ctx.send(f"{random.choice(responses)}")

@pip.command(aliases=['8ball', '8b'])
async def _8ball(ctx, *, question): #asterisk allows the input of multiple arguements
    responses=["It is certain.",
                "yes daddy",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "N-N-No baka >///<",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@pip.command()
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

# clear all reference code if amount == "all":
#     await ctx.send("Are you sure you want to delete all messages in this channel?")
# 
#     def check(message):
#         if message.author == ctx.author:
#           return ctx.author == message.author # Or just return True
# 
# 
#     try:
#        answer = await pip.wait_for("message", timeout = 20.0, check = check)
#        if answer == "yes":
#           await ctx.channel.purge(limit=100000000)
#        else:
#           await ctx.send("failed")
# 
#     except asyncio.TimeoutError:
#        await ctx.send('Timeout')
# 
#  else:


pip.run('token')
#again pip is used in pip.run bcuz it was declared as pip = commands.bot....
