import discord
from discord.ext import commands, tasks
import os
import inspect
import dotenv
import aiohttp


import cogs


from events.onReady import onReady


dotenv.load_dotenv()


class Setup(commands.Bot):
    def __init__(self):
        self.bot_id: int = int(os.getenv("BOT_ID"))
        self.token: str = os.getenv("TOKEN")
        self.guild_id: int = int(os.getenv("GUILD_ID"))
        super().__init__("!", intents=discord.Intents.all(), application_id=self.bot_id)

    async def setup_hook(self):
        self.session = aiohttp.ClientSession
        for cogName, cog in inspect.getmembers(cogs):
            if inspect.isclass(cog):
                await self.load_extension(f"cogs.{cogName}")
               await bot.tree.sync(guild=discord.Object(id=self.guild_id))

    async def on_ready(self):
        await onReady(self)


try:
    bot = Setup()
    bot.run(bot.token, reconnect=True)
except KeyboardInterrupt:
    print("\nExiting...")
