
import discord

import random

import os



from dotenv import load_dotenv


from discord.ext import commands


load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


bot = commands.Bot(command_prefix="+")
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Jupyter'))







@bot.event
async def on_message(message):
	
	if message.content == "hello":
		
		await message.channel.send("Hello,How are you?")






	await bot.process_commands(message)

  
@bot.command()
async def coolrate(ctx):
  embed = discord.Embed(title="CoolRate", description = f"You are {random.randrange(100)}% cool {ctx.author.mention}", color=discord.Color.random())
  await ctx.send(embed = embed)


@bot.command()
async def gayrate(ctx):
  embed = discord.Embed(title="GayRate", description = f"You are {random.randrange(100)}% gay {ctx.author.mention}", color=discord.Color.random())
  await ctx.send(embed = embed)


@bot.command(
	
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	
	brief="Prints pong back to the channel."
)
async def ping(ctx):

	await ctx.channel.send("pong")




  

@bot.command(
	
	help="Looks like you need some help.",

	brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = ""


	for arg in args:
		response = response + " " + arg


	await ctx.channel.send(response)


bot.run(DISCORD_TOKEN)
