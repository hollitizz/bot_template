from discord import Guild
from utils.types import BotType
import logging


_logger = logging.getLogger(__name__)


async def onGuildJoin(self: BotType, guild: Guild):
    _logger.info(f"Joined guild {guild.name} (id: {guild.id})")