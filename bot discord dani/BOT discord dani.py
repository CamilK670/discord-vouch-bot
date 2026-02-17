import discord
from discord.ext import commands
import json
import os

import os
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)

if os.path.exists("../pythonProject/vouches.json"):
    with open("../pythonProject/vouches.json", "r") as f:
        vouches = json.load(f)
else:
    vouches = {}


@bot.command()
async def vouch(ctx, member: discord.Member):
    if str(member.id) not in vouches:
        vouches[str(member.id)] = 0

    vouches[str(member.id)] += 1

    with open("../pythonProject/vouches.json", "w") as f:
        json.dump(vouches, f)

    new_name = f"{member.name} 『{vouches[str(member.id)]} Vouches ✅』"

    try:
        await member.edit(nick=new_name)
        await ctx.send(f"✅ {member.mention} a maintenant {vouches[str(member.id)]} vouches !")
    except:
        await ctx.send("❌ Je n'ai pas la permission de modifier le pseudo.")


bot.run(TOKEN)