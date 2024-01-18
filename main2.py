import discord, random , requests , os
from discord.ext import commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_name = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file was saved by{file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] == '70s\n' and hasil[1] >= 0.6:
                await ctx.send('This Is A 70s Photo')
                await ctx.send('Another Information...')
            elif hasil[0] == '80s\n' and hasil[1] >= 0.6:
                await ctx.send('This Is A 80s Photo')
                await ctx.send('Another Information...')
            elif hasil[0] == '90s\n' and hasil[1] >= 0.6:
                await ctx.send('This Is A 90s Photo')
                await ctx.send('Another Information...')
            else:
                await ctx.send('Invalid Pic :(')
    
    

    else:
        await ctx.send('You are Didnt Save Anything')


bot.run("MTEzNDEwNDIxODQzMzc0OTE1Mw.GUpGgh.lP6Iv8YHuYBec2DUlLqwSi8Gm9tsxvnDholB80")
