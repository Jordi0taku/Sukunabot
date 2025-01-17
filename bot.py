import discord
import random
import os
from discord.ext import commands
from bot_logic import gen_pass
from discord.ext import tasks
from bot_logic import get_duck_image_url
from bot_logic import get_fox

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("😞")

@bot.command()
async def commands(ctx):
    await ctx.send("$password:Te genera una contraseña aleatoria")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def addx(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)

@bot.command()
async def chiste(ctx):
    chistes = ["¿Cuál es el último animal que subió al arca de Noé? El del-fin.", "¿Cómo se dice pañuelo en japonés? Saka-moko.", "¿Cómo se dice disparo en árabe? Ahí-va-la-bala.", "¿Por qué las focas miran siempre hacia arriba? ¡Porque ahí están los focos!"]
    await ctx.send(random.choice(chistes))

@bot.command()
async def roll(int):
   number = random.randint(1,6)
   await ctx.send(number)
   

@bot.command()
async def meme(ctx):
    with open('python/image/meme1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def meme_aleatorio(ctx):
    meme_alet = random.choice(os.listdir("python/image"))
    with open(f'python/image/{meme_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def inventario(ctx):
    inventary = random.choice(os.listdir("weapons"))
    calidad = ["⬜Comun⬜", "🟩Poco comun🟩", "🟦Rara🟦", "🟪Epica🟪", "🟨Legendaria🟨"]
    with open(f'weapons/{inventary}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        weapons = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=weapons)
    await ctx.send("Calidad:", random.choice(calidad))

@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando fox, 
    el programa llama a la función get_fox'''
    image_url = get_fox()
    await ctx.send(image_url)

bot.run("TOKEN")
