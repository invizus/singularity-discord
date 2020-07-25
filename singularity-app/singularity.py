import discord
import asyncio
from discord.ext import commands
import profs
import yaml

Config = yaml.load(open("/var/config.yml", "r"), Loader=yaml.FullLoader)
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
        listf = profs.getProf(str(nick.id))
    except:
        await ctx.send("```Error: could not get list of professions.```")
        return
    await ctx.send("```{}\'s profession list:\n{}```".format(nick, listf))

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
        result = profs.addExp(str(member.id), skill, increment)
    except:
        await ctx.send("```Error: could not add exp to skill.```")
        return
    await ctx.send("```{}Increased/changed {}\'s prof {} experience by {}.```".format(result, member, skill, increment))

@bot.command(pass_context=True)
async def addskill(ctx, skill):
    """Add new talent."""
    member = ctx.message.author
    postIntoChat = "added new profession"
    try:
        result = profs.addProf(str(member.id), str(skill))
        if result != "OK":
            postIntoChat = result
    except:
        await ctx.send("```Error.```")
        return
    await ctx.send("```{} {}: {}.```".format(member, postIntoChat, skill))

@bot.command(pass_context=True)
async def initiate(ctx, newmember: discord.Member):
    """Add new people to our party."""
    member = ctx.message.author
    if member.id == botadmin:
        result = profs.initiate(newmember.id)
        if result == "Exists":
            await ctx.send("```Member has already been initiated.```")
        elif result == "OK":
            await ctx.send("New member initiated. Lets welcome {} !".format(newmember))
    else:
        await ctx.send("```Error.```")

@bot.command(pass_context=True)
async def whois(ctx, member : discord.Member):
    """Tells you members ID !whois <username>."""
    await ctx.send('{0.name} ID: {0.id}'.format(member))

bot.run(token)
