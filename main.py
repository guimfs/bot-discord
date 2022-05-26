import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from time import sleep

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f'Estou pronto! Estou conectado como {bot.user}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(976297540494438445)
    await channel.send(f'{member.name}, welcome to the third world!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(976297540494438445)
    await channel.send(f'Au revooir {member.name}, until soon!')

@bot.command(name='hello')
async def hello(ctx):
    name = ctx.author.name
    answer = 'Whats up, ' + name + '!' + " I'm the " + bot.user.name
    await ctx.send(answer)

@bot.command(name='ping')
async def ping(ctx):
    ping = round(bot.latency * 1000)
    await ctx.send(f'My ping is {ping} ms')

@bot.command(name='join')
async def join(ctx):
    if ctx.author.voice:
        if ctx.voice_client:
            await ctx.send("I'm already in the voice channel")
        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()
            await ctx.send(f"I'm connected to {ctx.message.author.voice.channel} voice channel")
    else:
        await ctx.send('Please, connect to a voice channel to call the Explorer Bot')

@bot.command(name='leave')
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send(f'I left the {ctx.message.author.voice.channel} voice channel')
    else:
        await ctx.send("I'm not in a voice channel")

@bot.command(name='1')
async def number_1(ctx):
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel
        vc = await voice_channel.connect()
        vc.play(FFmpegPCMAudio(executable="C:/FFmpeg/ffmpeg.exe", source="audio/are_you_ready.mp3"))
        while vc.is_playing():
            sleep(4)
        await vc.disconnect()
        await ctx.message.delete()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
        await ctx.message.delete()

bot.run("OTc5MjAyMTQyNTgzNzkxNjQ2.GUky5-.v3UXtoeeugEYiGqp5xpcIfYD-LEn3vGqiSUNaM")

