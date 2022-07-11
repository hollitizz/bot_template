from discord import Interaction, Member

async def ban(self, ctx: Interaction, member: Member, reason: str=None):
    await member.ban(reason=reason)
    await ctx.response.send_message(f"{member.mention} has been banned ! Reason: {reason}", ephemeral=True)