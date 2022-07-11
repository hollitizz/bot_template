from discord.ext import commands
import discord
import os

class Setup(commands.Bot):
    def __init__(self):
        self.bot_id: int = int(os.getenv("BOT_ID"))
        self.token: str = os.getenv("TOKEN")
        self.guild_id: int = int(os.getenv("GUILD_ID"))
        super().__init__("!", intents=discord.Intents.all(), application_id=self.bot_id)
