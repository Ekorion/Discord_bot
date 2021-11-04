import os
import discord
from array import array
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready(): # s'assurer que le bot est prêt
    print("Le bot est prêt.")

@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()


bot.run(os.getenv("TOKEN"))
