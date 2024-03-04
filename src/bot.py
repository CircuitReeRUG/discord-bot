import asyncio
import discord
from discord.ext import commands
from os import listdir, environ

TOKEN = environ.get("DISCORD_TOKEN")
guild_id = 1208551782133927987
intents = discord.Intents.all()


class Voltee(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents=intents,
        )

    async def load_extensions(self):
        for filename in listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")

    async def setup_hook(self):
        # Load extensions (cogs)
        await self.load_extensions()

        # Clear any previously set commands for the specified guild to avoid duplicates
        self.tree.clear_commands(guild=discord.Object(id=guild_id))

        # Synchronize the slash commands with Discord
        await self.tree.sync(guild=discord.Object(id=guild_id))


    async def on_ready(self):
        print("-------------------")
        print(f"Logged in as {bot.user}")
        print("-------------------")


if __name__ == "__main__":
    bot = Voltee()
    # Don't forget to export the token in environment :)
    bot.run(TOKEN, reconnect=True)
