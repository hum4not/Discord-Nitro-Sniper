print("humanot#1337 - https://discord.gg/xCHSTKJA5H")
import discord
from discord.ext import commands
import requests
from colorama import Fore
import re
TOKEN = ""
client = discord.Client()
client = commands.Bot(command_prefix="!",self_bot=True)
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}#{client.user.discriminator}\nSniping...")
@client.event
async def on_message(message):
    async for message in message.channel.history(limit=1): # <- way to bypass discord intents
        content = message.content
    def NitroData(code):
        print(
            f"{Fore.WHITE} - Channel: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - Server: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - Author: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - Code: {Fore.YELLOW}{code}"
            + Fore.RESET)
    from datetime import datetime
    time = datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in content:
        code = re.search("discord.gift/(.*)", content).group(1)
        headers = {'Authorization': TOKEN}
        r = requests.post(
            f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
            headers=headers,
        ).text
        if 'This gift has been redeemed already.' in r:
            print(""
                    f"\n{Fore.CYAN}[{time} - Nitro has been already redeemed" + Fore.RESET)
            NitroData(code)
        elif 'subscription_plan' in r:
            print(""
                    f"\n{Fore.CYAN}[{time} - Valid nitro]" + Fore.RESET)
            NitroData(code)
        elif 'Unknown Gift Code' in r:
            print(""
                    f"\n{Fore.CYAN}[{time} - Fake nitro]" + Fore.RESET)
            NitroData(code)
    else:
        return
client.run(TOKEN, bot=False, reconnect=True)