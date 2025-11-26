# Discord Project Helper Bot

Un bot Discord polyvalent conçu pour faciliter la gestion de projets de développement en fournissant un accès rapide à la documentation, aux ressources de design et à la gestion des tâches.

## Fonctionnalités

### Documentation Helper
- `/doc` - Affiche tous les liens importants du projet (GitHub, Discord, Figma)
- `/repo` - Accès rapide au repository GitHub
- `/stack` - Informations sur la stack technique utilisée

### Design Reminder
- `/figma` - Lien direct vers les maquettes Figma
- `/palette` - Palette de couleurs du projet
- `/typography` - Typographie et polices utilisées

### Task Management
- `/creat_tache` - Créer une nouvelle tâche pour un membre
- `/tache_list` - Afficher la liste de toutes les tâches

## Installation

### Prérequis
- Python 3.8 ou supérieur
- Un bot Discord (créé via le [Discord Developer Portal](https://discord.com/developers/applications))

### Configuration

1. **Cloner le repository**
```bash
git clone https://github.com/votre-repo/discord-bot.git
cd discord-bot
```

2. **Installer les Poetry**
```bash
poetry install
poetry shell 
```


3. **Configurer les variables d'environnement**

Créez un fichier `.env` à la racine du projet :
```env
DISCORD_BOT_TOKEN=votre_token_bot_discord_ici
ID_CHANNEL_ANNONCE=id_channel_annonce
```

4. **Lancer le bot**
```bash
poetry run python src/discord_bot/mainBot.py
```

## Structure du projet

```
.
├── src/
│   └── discord_bot/
│       ├── __init__.py
│       └── mainBot.py
├── tests/
├── .env
├── .example.env
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── README.md
└── taches.txt
```

## Configuration du bot

### Permissions requises
Le bot nécessite les permissions suivantes :
- Lire les messages
- Envoyer des messages
- Utiliser les commandes slash

### Intents Discord
Le bot utilise tous les intents (`discord.Intents.all()`). Pour un usage en production, il est recommandé de limiter aux intents strictement nécessaires.

## Utilisation des commandes

### Commandes de documentation
```
/doc          → Affiche tous les liens du projet
/repo         → Lien vers le repository GitHub
/stack        → Stack technique du projet
```

### Commandes de design
```
/figma        → Lien vers les maquettes Figma
/palette      → Palette de couleurs
/typography   → Informations typographiques
```

### Commandes de gestion des tâches
```
/creat_tache <nom_destinataire> <nom_tache>  → Créer une tâche
/tache_list                                   → Lister toutes les tâches
```

## Développement

### Technologies utilisées
- **discord.py** - Bibliothèque Python pour l'API Discord
- **python-dotenv** - Gestion des variables d'environnement
- **Poetry** - Gestionnaire de dépendances

### Contribuer
Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.