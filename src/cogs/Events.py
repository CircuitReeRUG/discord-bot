# Periodically checks for new events and posts them
from discord.ext import commands, tasks
from discord import Color, Embed, Status
import sys
sys.path.insert(0, 'cogs/scripts/')
from eventCheck import *
from randomStatus import random_liner
from random import choice 
from asyncio import sleep
import pytz, datetime

cet = pytz.timezone('CET')
time = datetime.time(hour=8, minute=30, tzinfo=cet)

COMMITTEE = "SporTee"
CHANNEL_ID = 1208551782616277025 # Ugly as hell, figure out a way to not hardcode this

def create_embeds(events:list[tuple]) -> list[Embed]:
    embeds = []
    
    for event in events:
        title = event[0]
        event = event[1]
        embed = Embed(title=title, description=event["description"], color=Color.random())
        embed.add_field(name="Date", value=event["date"], inline=True)
        embed.add_field(name="Time", value=event["time"], inline=True)
        embed.add_field(name="Location", value=event["location"], inline=True)
        embed.add_field(name="URL", value=event["link"], inline=True)
        embed.set_author(name=event["organizer"])
        embeds.append(embed)
    return embeds

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.start_tasks())
    
    def cog_unload(self):
        self.new_events.cancel()

    async def start_tasks(self):
        await self.bot.wait_until_ready()  # Wait until the bot is ready
        self.new_events.start()
    
    # Actual line
    # @tasks.loop(time=time)
    # Debug line
    @tasks.loop(seconds=10)
    async def new_events(self):
        await self.bot.change_presence(activity=random_liner(), status=Status.dnd)
        # Check for new events
        channel = self.bot.get_channel(CHANNEL_ID)
        await channel.send("Goodbye, cruel world.")
        if events := update_check(comm=COMMITTEE):
            # Debug, add to logging instead
            print(f"New event{'s' if len(events)> 1 else ''} found @ {datetime.datetime.now().strftime('%Y-%m-%d')}")
            # Get the channel to send the message to
            channel = self.bot.get_channel(CHANNEL_ID)
            # Create and post the embed(s)
            for embed in create_embeds(events):
                await channel.send(embed=embed)
                
            # Silently ping everyone (troll)
            # await channel.send("@everyone", delete_after=2)
    
        
# setup
async def setup(bot): # this is called by Pycord to setup the cog
    await bot.add_cog(Events(bot)) # add the cog to the bot