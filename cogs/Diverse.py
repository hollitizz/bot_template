from discord.ext import commands
from discord import app_commands, Interaction, Object, Member


from utils.types import Setup


from commands.diverse import ping
from commands.diverse import roll
from commands.diverse import ban


class Diverse(commands.Cog, description="Groupe de commande Divers"):
    def __init__(self, bot: Setup):
        self.bot = bot

    @app_commands.command(name="ping", description="Répond avec \"Pong !\"")
    async def ping(self, ctx: Interaction):
        await ping.ping(ctx)

    @app_commands.command(name="roll", description="Récuprer un nombre aléatoire entre deux nombres")
    @app_commands.describe(min="Minimum roll point, 1 by default", max="Maximum roll point, 6 by default")
    async def roll(self, ctx: Interaction, min: int=1, max: int=6):
        await roll.roll(self, ctx, min, max)

    @app_commands.command(name="ban", description="Ban a User")
    @app_commands.describe(user="User to ban", reason="Reason for the ban")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, ctx: Interaction, user: Member, reason: str=None):
        await ban.ban(self, ctx, user)

    @ban.error
    async def ban_error(self, ctx: Interaction, error: commands.CommandError):
        await ctx.response.send_message(f"{error}", ephemeral=True)


async def setup(bot: Setup):
    await bot.add_cog(Diverse(bot), guilds=[Object(id=bot.guild_id)])