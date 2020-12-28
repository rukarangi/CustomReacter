import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user}! Is here')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	print(message.author)

	#if message.content.startswith("$hello"):
	#	await message.channel.send("hello")
	#s	await message.add_reaction("😀")

	if message.author == "thukeeo#8811":
		print("its luke")
		await message.add_reaction("💩")

client.run("NzkzMDczOTUwOTcxNTI3MTY5.X-m9rA.kjKh6jf4fyyifMY0QGixkFnEtiQ")