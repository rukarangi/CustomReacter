import discord
import os
import re

from database import dbSession, User

client = discord.Client()

print(re.search("\$\w+\s*", "$helo"))

# store key on local machine
with open("key.txt") as f:
	key = f.read()

@client.event
async def on_ready():
	print(f'{client.user}! Is here')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	print(message.author)

	if message.content.startswith("$"):
		await messageHandler(message)
	else:
		if message.author.id == 276190242799616001:
			print("its luke")
			await message.add_reaction("💩")
			print(message.channel.permissions_for(message.author).administrator)

		if message.author.id == 471977641986228224:
			print("its pepep")
			await message.add_reaction("🇺")
			await message.add_reaction("🇷")
			await message.add_reaction("💩")

@client.event
async def on_reaction_add(reaction, user):
	print(user.id)
	msg = reaction.message
	print(msg.channel)
	if msg.author == client.user:
		await msg.channel.send("You reacted to me!")
	return


async def displayCommands(channel, m):
	embedMsg = discord.Embed(title="", description="List of Commmands:", color=0x00ff00)
	for key, com in m.items():
		embedMsg.add_field(name="$"+key, value=str(com.__doc__), inline=False)
	embedMsg.add_field(name="Source:", value="https://github.com/rukarangi/CustomReacter", inline=False)
	await channel.send(embed=embedMsg)


async def hello(message, m):
	"""
	Basic hello response for testing
	"""
	await message.channel.send("hello")
	await message.add_reaction("😀") 
	return

async def info(message, m):
	"""
	This displays this
	"""
	await displayCommands(message.channel, m)
	return

async def listUsers(message, m):
	"""
	Print out all users saved to db --Admin only
	"""
	admin = message.channel.permissions_for(message.author).administrator
	if admin:
		users = dbSession.query(User)
		msg = [user.as_dict() for user in users]
		print(msg)
	else:
		await message.channel.send("You do not have permission to use that command.")

	return

async def clearUsers(message, m):
	"""
	Print out all users saved to db --Admin only
	"""
	admin = message.channel.permissions_for(message.author).administrator
	if admin:
		dbSession.query(User).delete()
		dbSession.commit()
		await message.channel.send("Database has been removed of users.")
	else:
		await message.channel.send("You do not have permission to use that command.")

	return

def addUser(name, id, admin):
	user = User(name=name, id=id, admin=admin)
	dbSession.add(user)
	dbSession.commit()
	print(f"added user: {user}")
	return

async def badCommand(message, m):
	await message.channel.send("That is not a command i recognise, try '$help'")
	return

messages = {
	"hello": hello,
	"help": info,
	"list": listUsers
}


async def messageHandler(message):
	content = message.content
	author = message.author
	admin = message.channel.permissions_for(author).administrator
	
	#print(f'{author} admin:({admin}) : {content}')

	#command = message.content[1:5]
	command = re.search("\$\w+\s*", content).group()[1:]
	#print(command)
	command = "".join([s for s in command if s != " "])
	#print(command)

	func = messages.get(command, badCommand)
	await func(message, messages)

	return

client.run(key)