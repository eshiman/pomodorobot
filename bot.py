"""
bot.py
#TODO: remove globals
"""

import os

import asyncio
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
POM_STATUS = 'OFF'

bot = commands.Bot(command_prefix='pomodoro ')

def on_break():
    """ Returns text indicating current status of pomodoro"""
    minutes = datetime.now().minute
    if 25 <= minutes < 30:
        return "on break"
    if 55 < minutes < 60:
        return "on break"
    return "in a pomodoro session"

async def timer(ctx):
    """Pomodoro timer that lasts as long as POM_STATUS is ON"""
    global POM_STATUS
    POM_STATUS= 'ON'
    print("Timer has activated.")
    while POM_STATUS == 'ON':
        minutes = datetime.now().strftime("%M:%S")
        if (minutes in ['00:00','30:00']):
            status_message = "~~~\nPomodoro session starts now.\n" \
"To turn off pomodoro messages, type \"pomodoro off\" into the chat.\n~"
            await ctx.send(status_message)
        elif (minutes in ['25:00', '55:00']):
            status_message = "~~~\nTake a five minute break! " \
"Write what you have been doing for the last 25 minutes in the chat.\n~"
            await ctx.send(status_message)
        await asyncio.sleep(1)
    # when POM_STATUS is turned off, exit function
    print("Timer has deactivated.")

@bot.command(name='on', help='Turns on pomodoro timer')
async def pom_on(ctx):
    """Starts the pomodoro timer. Time of start does not impact pomodoro's schedule"""
    # If pomodoro is not already activated, turn it on
    if POM_STATUS != 'ON':
        response = "Pomodorobot messages are now visible. " \
"(To hide pomodoro messages from this channel, write \"pomodoro off\".)\n\n" \
"Concentration time begins at the start of (X:00) and midway through (X:30) each hour." \
"Every 25 minutes, there is a 5 minute break to chat. We are currently " \
+ on_break() + ". Happy playing!"
        await ctx.send(response)
        await timer(ctx)
    else:
        response = "Pomodoro is already on"
        await ctx.send(response)


@bot.command(name='off', help='Turns off pomodoro timer')
async def pom_off(ctx):
    """Turns off pomodoro timer"""
    global POM_STATUS
    POM_STATUS= 'OFF'
    response = "Pomodorobot messages are now invisible. " \
"(To turn pomodoro messages on, write \"pomodoro on\".)"
    await ctx.send(response)

bot.run(TOKEN)
