import praw
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from googlesearch import search 

client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.command()
async def reddit(ctx, sub):
    reddit = praw.Reddit(client_id="IK8dsacqxvvNbg", client_secret="Om7KubTddC6R3aKwHRHu27-QhUw", user_agent="bot by (/u/xsadia122")
    submission = reddit.subreddit(sub).random()
    await ctx.send(submission.title + " -> " + submission.url)
    
@client.command()
async def bye(ctx):
    author = ctx.author.mention
    await ctx.send(f'tchau, {author}')

@client.command()
async def Help(ctx):
    author = ctx.author.mention
    
    embed = discord.Embed(title = 'Lista De Comandos', colour=0xDEADBF)

    embed.set_author(name = "Ajudante do Fe")
    embed.add_field(name = '!googleSearch "sua pesquisa aqui" "quantidade de resultados desejados"', value = 'retorna as 5 primeiras respostas do google', inline=False)
    embed.add_field(name = '!sexta', value = 'A essencia da sexta-feira em forma de texto', inline=False)
    embed.add_field(name = '!reddit "subreddit"', value = 'Posta um Post aleatorio do reddit especificado', inline=False)
    embed.add_field(name = 'Palavras Especiais: rauster, ping, roi', value = 'Sempre que escritas no chat fazem algo', inline=False)
    

    await ctx.send(author, embed = embed)

@client.command()
async def googleSearch(ctx, query, numLink = 1):
    count = 1
    for j in search(query, tld="co.in", num=5, stop=numLink, pause=2):
        await ctx.send("=============================================================")
        await ctx.send(f'{count}' + ": " + j)
        count += 1
    await ctx.send("=============================================================")

@client.command()
async def sexta(ctx):
    await ctx.send("HJ É DIA DE GIRAR :cyclone: O COCO :coconut: BATER O CANECO HJ E DIA DE AFOGAR A TARTARUGA, A TARTARUGA :turtle: NUM GARRAFÃO COM SUCO :cup_with_straw: TRINK LIMÃO :lemon: E VODKA :flag_ru: HJ E DIA DE TRAVAR O NINTENDO :space_invader: DIA DE FAZER UMA ARVORE DE NATAL :christmas_tree: COM TODAS AS LATINHAS :beers: Q TU BEBEU HJ E DIA DE COCHILAR :zzz: NO BANHEIRO :toilet: E ACORDAR :ambulance: PERDIDA NO MEIO DA COZINHA :fork_knife_plate: COM UM SACO DE SUSPIRO NA MAO :ok_hand_tone1: VAMO DALEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE :trophy::santa_tone1:")
#===================================LEMBRAR DE TIRAR FUNCAO TEST================================================
@client.command()
async def test(ctx, arg):
    print("test Called")
    await ctx.send(f'{ctx.author.mention}'+ " " + arg)
#===============================================================================================================       
@client.command()
async def game(ctx, game):
    await client.change_presence(activity=discord.Game(name= game))

@client.event
async def on_ready():
    print("===========================================")
    print(f'{client.user} conectado com sucesso!')
    print("===========================================")
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "roi" in message.content.lower():
        await message.channel.send(f'{message.author.mention} vai toma no seu cu porra')

    if message.content.startswith('ping'):
        await message.channel.send(f'{message.author.mention} pong')
    
    if "rauster" in message.content.lower():
        await message.channel.send("eu odeio o Rauster")

    await client.process_commands(message)


client.run('NzM5OTA2NzMwMTkxODgwMzMy.XyhR1w.QkC-4l2kD87ahDqnpL_sygJOD3Y')