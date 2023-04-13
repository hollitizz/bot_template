from utils.SQLRequests import SQLRequests
from events import onReady, onMemberJoin, onMemberLeave, onGuildJoin, onGuildRemove
from utils.exportDatabase import exportDataBase
import cogs
import os
import inspect
import aiohttp
import discord
from discord.ext import commands, tasks
import logging


_logger = logging.getLogger(__name__)


class Bot(commands.Bot):
    def __init__(self):
        self.bot_id: int = int(os.getenv("BOT_ID"))
        self.token: str = os.getenv("TOKEN")
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(), application_id=self.bot_id
        )
        # uncomment this line to use a database
        # self.db = SQLRequests()

    async def setup_hook(self):
        self.session = aiohttp.ClientSession
        _logger.info("Loading commands...")
        for cogName, cog in inspect.getmembers(cogs):
            if inspect.isclass(cog):
                await self.load_extension(f"cogs.{cogName}")
        await self.tree.sync()
        _logger.info("Commands loaded")
    # uncomment those lines if you use a database
        # self.exportDataBaseTask.start()

    # @tasks.loop(hours=1)
    # async def exportDataBaseTask(self):
    #     exportDataBase()

    # @exportDataBaseTask.before_loop
    # async def before_exportDataBaseTask(self):
    #     await self.wait_until_ready()

    async def on_ready(self):
        await onReady.onReady(self)

    async def on_member_join(self, member: discord.Member):
        await onMemberJoin.onMemberJoin(self, member)

    async def on_raw_member_remove(self, payload: discord.RawMemberRemoveEvent):
        await onMemberLeave.onMemberLeave(self, payload)

    async def on_guild_join(self, guild: discord.Guild):
        await onGuildJoin.onGuildJoin(self, guild)

    async def on_guild_remove(self, guild: discord.Guild):
        await onGuildRemove.onGuildRemove(self, guild)