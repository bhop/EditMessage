import discord

token = "your token" # put your token here
clientID = "your client id" # put your client id here

class MyClient(discord.Client):
    async def on_ready(self):
        print("ready")
    async def on_message(self, message):
        print("e") # remove this if you want
        if message.author.id == clientID:
            await message.edit(content=message.content + " ")

client = MyClient()
client.run(token, bot=False)
