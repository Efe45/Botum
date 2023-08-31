import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('Mehmet Efe'):
        await message.channel.send("Dinliyorum")

    elif message.content.startswith(('YazıTuraAt')):
        yanit = random.choice(("yazi" , "tura"))
        await message.channel.send(yanit)
    
    elif message.content.startswith(('ZarAt')):
        zar = random.randint(1,6)
        await message.channel.send(zar)

    elif message.content.startswith(('SifreOlustur')):
        elements ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password = ""

        for i in range(10):
            password += random.choice(elements)
        
        
        await message.channel.send(password)
        
    else:
        await message.channel.send(message.content)

client.run("MTE0NDY1OTY2ODgyODk1MDU4OQ.GFq92h.aSdaFgVV1Kh6Ru_JfLOBUUzWXWBSzZWqyx2-E8")
