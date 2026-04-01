from discord.ext import commands

class Moderation(commands.Cog):
    @commands.hybrid_command(name="ban")
    async def ban(self, ctx, user):
        await ctx.send("ok")
