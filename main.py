

		
import discord

import random



import os

import keep_alive

from dotenv import load_dotenv

from discord_slash import SlashCommand


from discord.ext import commands


load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


bot = commands.Bot(command_prefix="+")
slash = SlashCommand(bot, sync_commands = True)
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

@bot.command(aliases=['8ball'])
async def eightball(ctx,*,question):
 responses  = ["It is certain.",
                "It is decidedly so.",
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
                "Outlook not so good.",
                "Very doubtful.",
                "Maybe."]
 await ctx.send(f':8ball: Answer: {random.choice(responses)}')  


 


    
  




@slash.slash(name="Ping", description="Ping Command")
async def Ping(ctx):
              

	await ctx.send("pong")






bot.run(DISCORD_TOKEN)

