from dis import dis, disco
import discord
from discord.ext import commands
import os
import inspect
import dotenv
import aiohttp
import logging

import cogs

from utils.DbHandler import DbHandler
from events import onReady, onMemberJoin, onMemberLeave


dotenv.load_dotenv()
discord.utils.setup_logging()

class Setup(commands.Bot):
    def __init__(self):
        self.bot_id: int = int(os.getenv("BOT_ID"))
        self.token: str = os.getenv("TOKEN")
        self.guild_id: int = int(os.getenv("GUILD_ID"))
        super().__init__("!", intents=discord.Intents.all(), application_id=self.bot_id)
        # DbHandler.__init__(self, "./memberWhitelist.json")

    async def setup_hook(self):
        self.session = aiohttp.ClientSession
        for cogName, cog in inspect.getmembers(cogs):
            if inspect.isclass(cog):
                logging.info(f"Loading {cogName} commands...")
                await self.load_extension(f"cogs.{cogName}")
                await bot.tree.sync(guild=discord.Object(id=self.guild_id))
                logging.info(f"{cogName} commands loaded!")

    async def on_ready(self):
        await onReady.onReady(self)

    async def on_member_join(self, member: discord.Member):
        await onMemberJoin.onMemberJoin(self, member)

    async def on_raw_member_remove(self, payload: discord.RawMemberRemoveEvent):
        await onMemberLeave.onMemberLeave(self, payload)

try:
    bot = Setup()
    bot.run(bot.token, reconnect=True, log_handler=None)
except KeyboardInterrupt:
    print("\nExiting...")
