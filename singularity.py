import discord
import asyncio
from discord.ext import commands
import profs
import yaml
### TODO
### 1. try/exception - somehow done
### 2. ability  add profs - done
### 3. backend to add users/remove profs - user add done

Config = yaml.load(open("config.yml", "r"))
token = Config['token']
botadmin = Config['admin']

description = '''There are few commands here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def skills(ctx, nick: discord.Member = None):
    """Do you have any special talents?"""
    if nick is None:
        nick = ctx.message.author
    try:
        listf = profs.getProf(nick.id)
    except:
        await bot.say("```Error happened.```")
        return
    await bot.say("```{}\'s profession list:\n{}```".format(nick, listf))

@bot.command(pass_context=True)
async def skill(ctx, skill, increment = None):
    """Add experience to skill. You can skill++ to up exp by 1, or !skill SkillName N. (Skill name is case sensitive)."""
    member = ctx.message.author
    if skill[-2:] == "++":
        skill = skill[:-2]
        increment = 1;
    elif skill[-2:] == "--":
        skill = skill[:-2]
        increment = -1;
    try:
#        result = profs.addExp(member.id, skill, int(increment))
        result = profs.addExp(member.id, skill, increment)
    except:
        await bot.say("```Error.```")
        return
    await bot.say("```{}Increased/changed {}\'s prof {} experience by {}.```".format(result, member, skill, increment))

@bot.command(pass_context=True)
async def addskill(ctx, skill):
    """Add new talent."""
    member = ctx.message.author
    postIntoChat = "added new profession"
    try:
        result = profs.addProf(member.id, str(skill))
        if result != "OK":
            postIntoChat = result
    except:
        await bot.say("```Error.```")
        return
    await bot.say("```{} {}: {}.```".format(member, postIntoChat, skill))

@bot.command(pass_context=True)
async def initiate(ctx, newmember: discord.Member):
    """Add new people to our party."""
    member = ctx.message.author
    if member.id == botadmin:
        result = profs.initiate(newmember.id)
        if result == "Exists":
            await bot.say("```Member has already been initiated.```")
        elif result == "OK":
            await bot.say("New member initiated. Lets welcome {} !".format(newmember))
    else:
        await bot.say("```Error.```")


@bot.command()
async def whois(member : discord.Member):
    """Tells you members ID !whois <username>."""
    await bot.say('{0.name} ID: {0.id}'.format(member))

bot.run(token)
