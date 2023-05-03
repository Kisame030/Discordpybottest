import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "ADD YOUR TOKEN HERE"
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("uyandım")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="selam")
async def selam(interaction: discord.Interaction):
    await interaction.response.send_message(f"Selam {interaction.user.mention}! slash command iste bu")

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "ne yazim")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} söylüyor: '{thing_to_say}'")
@bot.tree.command(name="sil") # Slash komutunu tanımlayın
async def sil(ctx, num:int): # Komutun argümanını tanımlayın (num)
    await ctx.channel.purge(limit=num) # Komutu gerçekleştirin (

bot.run(TOKEN)


