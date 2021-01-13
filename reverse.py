import discord

char = '\u202b'
token = "your token" # put your token here
clientid = "your client id" # put your client id here


class MyClient(discord.Client):
    async def on_ready(self):
        print("ready")
    async def on_message(self, message):
        print("e") # remove this if you want
        if message.author.id == clientid:
            await message.edit(content=f"{char} {message.content} {char}")

client = MyClient()
client.run(token, bot=False)



