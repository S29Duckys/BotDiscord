import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

print("Bot Launched")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
        print("Bot load")
        try:
                synced = await bot.tree.sync()
                print(f"{len(synced)} commandes slash synchronisées")
        except Exception as e:
                print(f"Erreur de synchronisation des commandes : {e}")


# Commandes Doc Helper
@bot.tree.command(name="doc", description="Obtenir les liens du projet")
async def doc(interaction: discord.Interaction):
        await interaction.response.send_message("**Liens du projet :**\n\n**GitHub :** https://github/repo.exemple\n**Discord :** https://discord.exemple\n**Figma :** https://figma.exemple")


@bot.tree.command(name="repo", description="Obtenir les liens du repo")
async def repo(interaction: discord.Interaction):
        await interaction.response.send_message("https://github/repo.exemple")


@bot.tree.command(name="stack", description="Obtenir les stack du projet")
async def stack(interaction: discord.Interaction):
        await interaction.response.send_message("pls qlq pour ecrire les stack svp")




# Commandes Design Reminder

@bot.tree.command(name="figma", description="Obtenir le lien Figma")
async def figma(interaction: discord.Interaction):
        await interaction.response.send_message("https://figma.exemple")

@bot.tree.command(name="palette", description="Obtenir la palette de couleurs")
async def palette(interaction: discord.Interaction):
        await interaction.response.send_message("palette")

@bot.tree.command(name="typography", description="Obtenir la typographie utilisée")
async def typography(interaction: discord.Interaction):
        await interaction.response.send_message("typo")

# Commandes task management
@bot.tree.command(name="creat_tache", description="creer une tache")
async def creat_tache(interaction: discord.Interaction, name_destinataire: str, tache_name: str):
        with open("taches.txt", "w+") as file:
                file.write(f"Tache cree pour : {name_destinataire} Tache : {tache_name}\n")
        await interaction.response.send_message(f"tache {tache_name} cree pour {name_destinataire} a bien ete ajoutee.")



@bot.tree.command(name="tache_list", description="Obtenir la liste des taches")
async def tache_list(interaction: discord.Interaction,):
        with open("taches.txt", "r") as file:
                taches = file.readlines()
        if taches:
                tache_message = "Liste des taches:\n" + "".join(f"- {tache.strip()}\n" for tache in taches)
        else:
                tache_message = "Aucune tache disponible."
        await interaction.response.send_message(tache_message)



bot.run(discord_token)