from host import keep_alive
import discord
from discord.ext import commands
from reddit import retterreddit

intents = discord.Intents.default()
retter = commands.Bot(command_prefix='.', intents=intents)


@retter.event
async def on_ready():
    print("Logged.")
    presence = discord.Game("Ban me now, Marvin")
    await retter.change_presence(status=discord.Status.do_not_disturb, activity=presence)


@retter.command()
async def reddit(ctx):
    await ctx.send(retterreddit())


@retter.event
async def on_message(ctx):
    ctx.content.lower()
    if ctx.author == retter.user:
        return
    if "bom dia" in ctx.content:
        await ctx.channel.send("bom dia")
    await retter.process_commands(ctx)

keep_alive()
retter.run('OTM5MTg4NTUzNDIwODAwMDYz.Yf1NgA.uHbwpsUrKhAXpG9jzcT6n3SkqNw')
