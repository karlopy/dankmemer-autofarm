import os
import sys

os.system("cls")
os.system(f"title Welcome to Vex Self Bot!")

import discord
import random
import asyncio
import json
import time
from datetime import datetime
from discord.ext import commands
from colorama import Fore



if json.load(open("config/config.json"))["token"] == "":
    os.system("cls")
    print("")
    print("Enter Discord Token below:".center(os.get_terminal_size().columns))
    print("")
    token = input()


    config = json.load(open("config/config.json"))
    config["token"] = (token)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)
if json.load(open("config/config.json"))["prefix"] == "":
    os.system("cls")
    print("")
    print("Enter Prefix: ".center(os.get_terminal_size().columns))
    print("")
    token = input()

    config = json.load(open("config/config.json"))
    config["prefix"] = (token)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)
if json.load(open("config/config.json"))["prefix"] == "":
    os.system("cls")
    print("")
    print("Enter Grinding Channel ID: ".center(os.get_terminal_size().columns))
    print("")
    token = int(input())

    config = json.load(open("config/config.json"))
    config["channelid"] = (token)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)


TOKEN = json.load(open("config/config.json"))["token"]
PREFIX = json.load(open("config/config.json"))["prefix"]
CHANNELID = json.load(open("config/config.json"))["channelid"]



bot = commands.Bot(command_prefix=PREFIX, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    os.system("cls")
    os.system(f"title Vex Bot ─ karlo#7777")
    print('\n')
    print(f"{Fore.GREEN}██╗   ██╗███████╗██╗  ██╗".center(os.get_terminal_size().columns))
    print(f"{Fore.GREEN}██║   ██║██╔════╝╚██╗██╔╝".center(os.get_terminal_size().columns))
    print(f"{Fore.GREEN}╚██╗ ██╔╝█████╗   ╚███╔╝ ".center(os.get_terminal_size().columns))
    print(f"{Fore.GREEN} ╚████╔╝ ██╔══╝   ██╔██╗ ".center(os.get_terminal_size().columns))
    print(f"{Fore.GREEN}  ╚██╔╝  ███████╗██╔╝╚██╗".center(os.get_terminal_size().columns))
    print(f"{Fore.GREEN}   ╚═╝   ╚══════╝╚═╝  ╚═╝".center(os.get_terminal_size().columns))
    print("")
    print(f"{Fore.WHITE}Vex Bot logged into {bot.user.name}".center(os.get_terminal_size().columns))


    autoReady = input(f'{Fore.WHITE}Enter \'start\' to start grinding Dank Coins!: ').lower()
    if autoReady == 'start':

        channel = bot.get_channel(CHANNELID)
        print(f'{Fore.GREEN}Starting to grind Dank Coins!')
        while True:
            await channel.send("pls hunt")
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Hunted!')
            await channel.send("pls search")
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Searched!')
            time.sleep(1)
            await channel.send("pls fish")
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Fished!')
            await channel.send("pls beg")
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Begged!')
            await channel.send("pls pm")
            await channel.send('f')
            time.sleep(1)
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]PMed!')
            await channel.send("pls beg")
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Begged!')
            await channel.send("pls hl")
            await channel.send("low")
            time.sleep(1)
            await channel.send("pls dep all")
            time.sleep(60)


@bot.event
async def on_message(message):
        #if message.author == client.user:
        #    return
        channel = bot.get_channel(CHANNELID)
        if message.author.id == 270904126974590976 and message.channel.id == CHANNELID:
            message.content = message.content.replace('﻿','')
            if "god forbid" in message.content:
                print("Interacted with a Dragon !")
            if "EVENT TIME WOO!" in message.content:
                print("Interacting with a Event !")
            if "street" in message.content:
                time.sleep(1)
                await channel.send("street")
            if "couch" in message.content:
                time.sleep(1)
                await channel.send("couch")
            if "sink" in message.content:
                time.sleep(1)
                await channel.send("sink")
            if "christmas tree" in message.content:
                time.sleep(1)
                await channel.send("christmas tree")
            if "fridge" in message.content:
                time.sleep(1)
                await channel.send("fridge")
            elif "north pole" in message.content:
                time.sleep(1)
                await channel.send("north pole")
            elif "discord" in message.content:
                time.sleep(1)
                await channel.send("discord")
            elif "christmas card" in message.content:
                time.sleep(1)
                await channel.send("christmas card")
            elif "big bait catches big fish" in message.content:
                time.sleep(1)
                await channel.send("big bait catches big fish")
            elif "What type of meme do you want to post?" in message.content:
                time.sleep(1)
                await channel.send("k")
            elif "yes please" in message.content:
                time.sleep(1)
                await channel.send("yes please")
            elif "oh look a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh look a dragon")
            elif "tree" in message.content:
                time.sleep(1)
                await channel.send("tree")
            elif "oh frick a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh frick a dragon")
            elif "make snow angel" in message.content:
                time.sleep(1)
                await channel.send("make snow angel")                                             
            elif "frick off" in message.content:
                time.sleep(1)
                await channel.send("frick off")
            elif "glub glub glub" in message.content:
                time.sleep(1)
                await channel.send("glub glub glub")
            elif "mistletoe" in message.content:
                time.sleep(1)
                await channel.send("mistletoe")
            elif "krampus is a nerd" in message.content:
                time.sleep(1)
                await channel.send("krampus is a nerd")
            elif "push" in message.content:
                time.sleep(1)
                await channel.send("push")
            elif "dibs" in message.content:
                time.sleep(1)
                await channel.send("dibs")
            elif "happy holidays" in message.content:
                time.sleep(1)
                await channel.send("happy holidays")
            elif "throw snowball" in message.content:
                time.sleep(1)
                await channel.send("throw snowball")
            elif "get the camera ready" in message.content:
                time.sleep(1)
                await channel.send("get the camera ready")
            elif "whoville sucks" in message.content:
                time.sleep(1)
                await channel.send("whoville sucks")
            elif "build snowman" in message.content:
                time.sleep(1)
                await channel.send("build snowman")
            elif "hook line sinker" in message.content:
                time.sleep(1)
                await channel.send("hook line sinker")
            elif "dog" in message.content:
                time.sleep(1)
                await channel.send("dog")
            elif "pantry" in message.content:
                time.sleep(1)
                await channel.send("pantry")
            elif "mailbox" in message.content:
                time.sleep(1)
                await channel.send("mailbox")
            elif "dresser" in message.content:
                time.sleep(1)
                await channel.send("dresser")
            elif "uber" in message.content:
                time.sleep(1)
                await channel.send("uber")
            elif "grass" in message.content:
                time.sleep(1)
                await channel.send("grass")
            elif "pocket" in message.content:
                time.sleep(1)
                await channel.send("pocket")
            elif "laundromat" in message.content:
                time.sleep(1)
                await channel.send("laundromat")
            elif "bed" in message.content:
                time.sleep(1)
                await channel.send("bed")
            elif "air" in message.content:
                time.sleep(1)
                await channel.send("air")
            elif "f in chat" in message.content:
                await channel.send("f in chat")
            elif "fuck off karen" in message.content:
                await channel.send("fuck off karen")
            elif "i am so very bored" in message.content:
                await channel.send("i am so very bored")
            elif "wear a mask god damn it" in message.content:
                await channel.send("wear a mask god damn it")
            elif "dragon these nuts on your momma" in message.content:
                await channel.send("dragon these nuts on your momma")
            elif "dragon says rawr" in message.content:
                await channel.send("dragon says rawr")       
            elif "why didn't I just go fishing" in message.content:
                await channel.send("why didn't I just go fishing")


bot.run(TOKEN, bot=False)
