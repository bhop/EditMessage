import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("ready")
    async def on_message(self, message):
        print("e")
        if message.author.id == CLIENT ID:
            await message.edit(content=message.content + " ")

client = MyClient()
client.run("TOKEN HERE", bot=False)
