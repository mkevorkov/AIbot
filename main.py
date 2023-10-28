import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"We have logged in as{bot.user}")
 
def get_duck_image_url():
     url = "https://random-d.uk/api/random"
     res = requests.get(url)
     data = res.json()
     return data["url"]


@bot.command("duck")
async def duck(ctx):
    '''По команде duck возвращает фото утки'''
    print("hello")
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachemt.url
            await attachemt.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./(atachment.filename)"))
    else:
        await ctx.send("Вы забыли загрузить картинку:(")
        
        
bot.run('MTE2NDEwMjk1NDMzMzI0MTM0NA.GuVbyA.hlEA-HWQXWj5zwIBORhXKxks3VC8WyAW3eukWs')