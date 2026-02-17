import discord
from discord.ext import commands
import json
import os

# ===== TOKEN =====
TOKEN = os.getenv("TOKEN")

# ===== INTENTS =====
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)

# ===== CHARGEMENT DES VOUCHES =====
vouches = {}

if os.path.exists("vouches.json"):
    try:
        with open("vouches.json", "r", encoding="utf-8") as f:
            vouches = json.load(f)
    except:
        vouches = {}
else:
    with open("vouches.json", "w", encoding="utf-8") as f:
        json.dump({}, f)

# ===== COMMANDE VOUCH =====
@bot.command()
async def vouch(ctx, member: discord.Member):
    if str(member.id) not in vouches:
        vouches[str(member.id)] = 0

    vouches[str(member.id)] += 1

    with open("vouches.json", "w", encoding="utf-8") as f:
        json.dump(vouches, f, indent=4)

    new_name = f"{member.name} 『{vouches[str(member.id)]} Vouches ✅』"

    try:
        await member.edit(nick=new_name)
        await ctx.send(f"✅ {member.mention} a maintenant {vouches[str(member.id)]} vouches !")
    except:
        await ctx.send("❌ Je n'ai pas la permission de modifier le pseudo.")

# ===== LANCEMENT =====
bot.run(TOKEN)
