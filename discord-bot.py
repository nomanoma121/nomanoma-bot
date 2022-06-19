import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def test(ctx):
    await ctx.send("test.ok!")


bot.run("OTg3NDQwMDAxOTQxOTE3NzM2.GiVcaY._-j_U85ZuzpGcMWcCZHv4htM4QnAFEkoL1tINM")