import os
import discord
from array import array
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")

client = commands.Bot(command_prefix="!")
warn = [0, 0]


@client.event
async def on_ready(): # s'assurer que le bot est prêt
    print("Le bot est prêt.")


@client.event
async def on_message(message):
    global warn
    member = {"test#1234": warn[0], "test2#4321": warn[1]}
    role = discord.utils.get(message.guild.roles, name='Mute')
    src = message.author
    if message.content.lower() == "logo":# si l'utilisateur poste logo

        if str(src) == "test#1234":
            warn[0] += 1
            await message.channel.send(f"Attention c'est ton avertissement numéro {warn[0]} ! https://tenor.com/view/finger-threathening-chiyaan-dhool-warn-gif-14013096")
        if str(src) == "test2#4321":
            warn[1] += 1
            await message.channel.send(f"Attention c'est ton avertissement numéro {warn[1]} ! https://tenor.com/view/joker-dont-say-i-didnt-warn-you-gif-15366592" )
        print(member[str(src)], member["test2#4321"])

        if warn[0] == 3:
            await message.channel.send("Je t'avais prevenu ! Maintenant tu es mute pour une heure !", delete_after=3600)
            await src.add_roles(role)
            warn[0] = 0
        if warn[1] == 3:
             await message.channel.send("Je t'avais prevenu ! Maintenant tu es mute pour une heure !", delete_after=3600)
             await src.add_roles(role)
             warn[1] = 0
client.run(os.getenv("TOKEN"))

