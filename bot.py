import discord
from discord.ext import commands

# Deine Bot-Token hier einfügen
TOKEN = "Your Token <3"
GUILD_ID = ServerID  # Die Server-ID (GUILD_ID) deines Servers hier einfügen
# Intents erstellen und die gewünschten Ereignisse aktivieren
# Intents erstellen und die gewünschten Ereignisse aktivieren
intents = discord.Intents.default()
intents.members = True  # Mitglieder-Intent aktivieren, um Mitglieder-Updates zu erhalten

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}')
    
    guild = bot.get_guild(GUILD_ID)
    role = discord.utils.get(guild.roles, name="muted")

    if role is None:
        print("Die Rolle 'muted' wurde nicht gefunden.")
        return

    banned_users = []

    for member in guild.members:
        if role in member.roles:
            try:
                await member.ban(reason="Muted role detected during bot startup.")
                banned_users.append(member)
            except discord.Forbidden:
                print(f"Der Benutzer {member.display_name} konnte nicht gebannt werden.")

    print(f"Folgende Benutzer mit der Rolle 'muted' wurden beim Start gebannt: {', '.join([member.display_name for member in banned_users])}")

bot.run(TOKEN)
