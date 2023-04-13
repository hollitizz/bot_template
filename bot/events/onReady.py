import logging
import discord

from utils.types import BotType


async def onReady(self: BotType):
    await self.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="configure me in bot/events/onReady.py"
        )
    )
    logging.info(f"{self.user} is Ready !")
