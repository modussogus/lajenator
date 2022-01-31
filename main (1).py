import discord
import sys
import random
import pydub
from pydub import AudioSegment
from discord.ext import commands
from discord.utils import get
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps
from termcolor import colored
import colorama
from discord_components import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient



client = commands.Bot(command_prefix = ">" , case_insensitive = 
True)
i = 0


@client.event
async def on_ready():
 print('soy {0.user}' .format (client))
 DiscordComponents(client)

@client.command()
async def viva(ctx):
  await ctx.send(f'vai toma no cu, {ctx.author}')



@client.command()
async def a(ctx):
  await ctx.send('frifrare')  

@client.command()
async def teste2(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/806463233539964939/865544588181897226/Bodiafamilia.mp4') 

@client.command()
async def tilapia(ctx):  
  await ctx.send('https://media.discordapp.net/attachments/168765552938975232/853010218728423516/s.gif')

@client.command()
async def desgraca(ctx , arg):  
  await ctx.send(arg)

@client.command()
async def quemepedro(ctx):  
  await ctx.send("بيدرو هو الشيطان ، الشرير المتجسد ، أسوأ شيء تم إنشاؤه على الإطلاق ، لديه أكثر من مليون دعوى قضائية باسمه وهو مثلي جنسيًا جدًا ، وارتكب خمسمائة واثنين وثمانين جريمة حرب وقتل واحدًا وعشرين طفلاً في إفريقيا")

@client.command()
async def trabalhe(ctx):
  await ctx.send('nao')  

@client.command()
async def amogus(ctx):
  await ctx.send('https://tenor.com/view/19dollar-fortnite-card-among-us-amogus-sus-red-among-sus-gif-20549014')  

img = Image.open("b.jpg")
img.show()

@client.command() 
async def test(ctx):
  await ctx.send("s")

@client.command()
async def soma(ctx, a: float, b: float):
  await ctx.send(a + b)

@client.command()
async def maior(ctx, a: float, b: float):
  await ctx.send(max(a,b))


@client.command()
async def menos(ctx, a: float, b: float):
  await ctx.send(a - b)

@client.command()
async def mult(ctx, a: float , b: float):
  await ctx.send(a * b)

@client.command()
async def dividir(ctx, a: float, b: float):
 if (b == 0 or inf ):
   await ctx.send("sim")
 else:
   await ctx.send(a / b)

@client.command()
async def delta(ctx, a: int, b: int, c: int):
  await ctx.send((b*b) - 4 * a * c )

@client.command()
async def raiz(ctx, a: int):
 if (a < 0):
   await ctx.send("raiz de numero negativo é foda")
 else:
   await ctx.send(math.sqrt(a))

@client.command()
async def ultimato(ctx, b: int, delta : int,
a : int):
  await ctx.send((-b + (math.sqrt(delta) / 2*a)))

@commands.has_permissions(administrator=True)
@client.command()
async def testedeeveryone(ctx):
 await ctx.send('nao')

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def cargo(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)

@commands.has_role("Administrador") 
@client.command(pass_context=True)
async def shutdown(ctx):
    await ctx.send("nao")

@client.command()
async def spam(ctx , arg, x: int):
 for x in range(1,x+1):
   if (arg.find("@everyone" or "<@!560548543664750592>") == -1):
    await ctx.send(arg)
    print (arg)
   else:
    await ctx.send("não xd")
 
@client.command()
async def DM(ctx, user: discord.User, message=None):
    message = message or "sexo"
    await user.send(message)

@client.command()
async def DMspam(ctx , user: discord.User,  message=None,*,s: int):
  for s in range(1,s+1):
    await user.send(message)

@client.command()
async def kickcall(ctx, member: discord.Member):
  while i < 9999:
   {
   await member.move_to(None)
   }
@client.command()
async def testcall(ctx, member: discord.Member, call):
  await member.move_to(call)


@client.command()
async def end(ctx):
  await exit.spam()

@client.command()
async def rand(ctx, a : int , b: int):
  await ctx.send(random.randint(a , b))

  
@commands.has_permissions(ban_members = True)
@client.command()
async def ban(ctx,user : discord.Member):
  if (user == 560548543664750592):
     ctx.send("nao")
  else:
    await discord.Member.ban(user)



@commands.has_permissions(ban_members = True)
@client.command()
async def kick(ctx, user : discord.Member):
  await discord.Member.kick(user)



@client.command()
async def custombotao(ctx, arg):
   await ctx.send(
    "a",
    components= [
       Button(label = arg)
    ]
 )




@client.command(pass_context = True)
async def fotoperfil(ctx ,*, user : discord.Member = None):
  pfp = user.avatar_url
  await ctx.send(pfp)


@commands.has_permissions(ban_members = True)
@client.command()
async def acordabaiano(ctx):
     while i < 1:{
    await ctx.send("@everyone")
   }

@client.command()
async def repl(ctx, arg):
  exec(arg)

@client.command()
async def delchat(ctx, channel):
  await ctx.send("nao")
  

@client.command()
async def musicas(ctx):
  musicas = ["sexo.mp3","superidol.mp3","zapzap.mp3","flamengo.mp3","yharon.mp3"]
  await ctx.send(musicas)

@client.command(pass_context = True)
async def musica(ctx, musica=""):
  server = ctx.message.guild.voice_client

  channel = ctx.message.author.voice.channel
  vc = await channel.connect()
  vc.play(discord.FFmpegPCMAudio(musica), after=lambda e: print('done', e)
  )


@commands.has_permissions(ban_members = True)
@client.command()
async def rolle(ctx,nome,cor : int,vezes : int):
  for i in range(1,vezes):
   await ctx.guild.create_role(name=nome,color=cor)  
  
@commands.has_permissions(ban_members = True)
@client.command()
async def delrole(ctx,*,role : discord.Role = None):
  await role.delete()


@client.command()
async def ceara(ctx):
  await ctx.send(b.png)


client.run('tokenxd')

