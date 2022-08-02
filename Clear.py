import discord
import os
from discord.ext import commands
import pystyle

intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)
os.system("title Clear - By: Black spy")
token = input("Token: ")
prefix = "."
os.system('cls' if os.name == 'nt' else 'clear')
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    pystyle.Write.Print(f'''
 ░█████╗░██╗░░░░░███████╗░█████╗░██████╗
 ██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗
 ██║░░╚═╝██║░░░░░█████╗░░███████║██████╔╝
 ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██╔══██╗
 ╚█████╔╝███████╗███████╗██║░░██║██║░░██║
 ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
                 Logando como: {bot.user}
                     use o comando: .clear
''',
                        color=pystyle.Colors.black_to_white,
                        interval=0.0001)

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    ping = round(bot.latency * 1000)
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                mensagem = msg.content
                print(f"{pystyle.Colors.green}[✅] {pystyle.Colors.white}{mensagem} {pystyle.Colors.green}| {pystyle.Colors.white}{ctx.channel} {pystyle.Colors.green}| {pystyle.Colors.white} ping: {pystyle.Colors.purple}{ping}")
                await msg.delete()
                passed += 1
            except:
                mensagem = msg.content
                print(f"{pystyle.Colors.red}[❌] {pystyle.Colors.white}{mensagem} {pystyle.Colors.red}| {pystyle.Colors.white}{ctx.channel} {pystyle.Colors.red}| {pystyle.Colors.white} ping: {pystyle.Colors.purple}{ping}")
                failed += 1
    print(f"\n{pystyle.Colors.green}[{pystyle.Colors.white}Completo{pystyle.Colors.green}] {pystyle.Colors.white}Removido {pystyle.Colors.green}{passed}{pystyle.Colors.white} mensagens com {pystyle.Colors.red}{failed} {pystyle.Colors.white}falha")

bot.run(token, bot=False)
