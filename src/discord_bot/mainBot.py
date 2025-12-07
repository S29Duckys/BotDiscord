import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime 
load_dotenv()

discord_token = os.getenv("DISCORD_BOT_TOKEN")
id_channel_annonce = int(os.getenv("ID_CHANNEL_ANNONCE"))

print("Bot Launched")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Event demarage du bot

@bot.event
async def on_ready():
        print("Bot load")
        try:
                synced = await bot.tree.sync()
                print(f"{len(synced)} commandes slash synchronisées")
                channel = bot.get_channel(id_channel_annonce)
                # if channel:
                #         await channel.send("```Bot en ligne```")
                # else:
                #         print("Channel non trouvé.")
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

@bot.tree.command(name="creat_tache", description="créer une tâche")
async def creat_tache(
    interaction: discord.Interaction, 
    name_destinataire: str, 
    tache_name: str, 
    content_tache: str
):
    # Charger les tâches existantes
    if os.path.exists("taches.json"):
        with open("taches.json", "r", encoding="utf-8") as file:
            try:
                taches = json.load(file)
            except json.JSONDecodeError:
                # Si le fichier est corrompu, on repart de zéro
                taches = []
    else:
        taches = []
    
    # Générer automatiquement l'ID
    if taches:
        id_tache = max(t["IdTache"] for t in taches) + 1
    else:
        id_tache = 1
    
    # Créer la nouvelle tâche
    nouvelle_tache = {
        "IdTache": id_tache,
        "Destinataire": name_destinataire,
        "Tache": tache_name,
        "Contenu": content_tache,
        "Statut": "En attente",
        "CreePar": interaction.user.name,
        "DateCreation": datetime.now().isoformat()
    }
    
    taches.append(nouvelle_tache)
    
    # Sauvegarder dans le fichier
    with open("taches.json", "w", encoding="utf-8") as file:
        json.dump(taches, file, indent=2, ensure_ascii=False)
    
    print(f"Tâche créée : {nouvelle_tache}")
    
    # Réponse avec embed
    embed = discord.Embed(
        title=f"Tâche #{id_tache} créée",
        color=discord.Color.green()
    )
    embed.add_field(name=" Tâche", value=tache_name, inline=False)
    embed.add_field(name=" Contenu", value=content_tache, inline=False)
    embed.add_field(name=" Destinataire", value=name_destinataire, inline=True)
    embed.add_field(name=" Créée par", value=interaction.user.mention, inline=True)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="tache_list", description="Obtenir la liste des tâches")
async def tache_list(interaction: discord.Interaction):
    # Vérifier si le fichier existe
    if not os.path.exists("taches.json"):
        await interaction.response.send_message("Aucune tâche disponible.")
        return
    
    # Lire le fichier JSON
    with open("taches.json", "r", encoding="utf-8") as file:
        try:
            taches = json.load(file)  # ← Utiliser json.load()
        except json.JSONDecodeError:
            await interaction.response.send_message("Fichier JSON invalide.")
            return
    
    # Vérifier s'il y a des tâches
    if not taches:
        await interaction.response.send_message("Aucune tâche disponible.")
        return
    
    # Construire le message en bouclant sur chaque tâche
    tache_message = "**Liste des tâches :**\n\n"
    
    for tache in taches:  # ← IMPORTANT : Boucler sur chaque tâche
        tache_message += f"** ID :** {tache['IdTache']}\n"
        tache_message += f"** Destinataire :** {tache['Destinataire']}\n"
        tache_message += f"** Tâche :** {tache['Tache']}\n"
        tache_message += f"** Contenu :** {tache.get('Contenu', 'Pas de contenu')}\n"
        tache_message += "─────────────────\n"
    
    await interaction.response.send_message(tache_message)

@bot.tree.command(name="del_tache", description="Supprimer une tâche")
async def del_tache(interaction: discord.Interaction, id_tache: int):
    if not os.path.exists("taches.json"):
        await interaction.response.send_message("Aucune tâche trouvée.")
        return
    
    # Lire les tâches
    with open("taches.json", "r", encoding="utf-8") as file:
        try:
            taches = json.load(file)
        except json.JSONDecodeError:
            await print("Fichier JSON invalide.")
            return
    
    # Filtrer : garder toutes les tâches SAUF celle avec l'ID à supprimer
    taches_avant = len(taches)
    taches = [t for t in taches if t['IdTache'] != id_tache]
    taches_apres = len(taches)
    
    # Vérifier si une tâche a été supprimée
    if taches_avant == taches_apres:
        await interaction.response.send_message(f"La tâche #{id_tache} n'existe pas.")
        return
    
    # Sauvegarder
    with open("taches.json", "w", encoding="utf-8") as file:
        json.dump(taches, file, indent=2, ensure_ascii=False)
    
    await interaction.response.send_message(f"Tâche **#{id_tache}** supprimée avec succès !")

# Event de deconnexion

@bot.tree.command(name="kill", description="kill le bot")
async def kill(interaction: discord.Interaction):
        await interaction.response.send_message("Le bot va se deconnecter.")
        await bot.close()
        print("Bot deconnecte.")

@bot.event 
async def on_disconnect():
    try:
        channel = bot.get_channel()
        if channel and not bot.is_closed(id_channel_annonce):
            await channel.send("```Bot hors ligne```")
    except Exception as e:
        pass

bot.run(discord_token)