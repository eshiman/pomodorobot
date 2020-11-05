# bot.py
import os

import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
pom_status = 'OFF'
pom_init_time = '00:00:00'

bot = commands.Bot(command_prefix='pomodoro ')

@bot.command(name='on', help='Show pomodoro messages')
async def pom_on(ctx):
    global pom_status
    global pom_init_time
    pom_status= 'ON'
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response = "Pomodorobot messages are now visible. (To hide pomodoro messages from this channel, write \"pomodoro off\".)\n\nConcentration time begins at the start of (X:00) and midway through (X:30) each hour. Every 25 minutes, there is a 5 minute break to chat. We are currently " + on_a_break() + ". Happy playing!" 
    await ctx.send(response)
    await timer(ctx)

@bot.command(name='off', help='Hide pomodoro messages')
async def pom_on(ctx):
    global pom_status
    pom_status= 'OFF'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response = "Pomodorobot messages are now invisible. To turn pomodoro messages on, write \"pomodoro on\"."
    await ctx.send(response)
        
async def timer(ctx):
    while (pom_status == 'ON'):
        now = datetime.now()
        print(now)
        minutes = now.strftime("%M:%S")
        current_time = now.strftime("%H:%M:%S")
        if (minutes == '00:00' or minutes == '30:00'): 
            response = "Pomodoro session starts now. Play for 25 minutes." 
            await ctx.send(response)
        elif (minutes == '25:00' or minutes == '30:00'): 
            response = "Take a five minute break! Write what you have been doing for the last 25 minutes in the chat."
            await ctx.send(response)
        await asyncio.sleep(1)

def on_a_break():
    now = datetime.now()
    minutes = now.minute
    if (minutes >= 25 and minutes < 30):
        return "on a break"
    if (minutes > 55 and minutes < 60):
        return true
    return "in a pomodoro session"
        

bot.run(TOKEN)
