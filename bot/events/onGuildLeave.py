from discord import Guild
from utils.types import BotType
import logging


_logger = logging.getLogger(__name__)


async def onGuildLeave(self: BotType, guild: Guild):
    _logger.info(f"Leave guild {guild.name} (id: {guild.id})")