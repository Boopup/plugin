import discord
from discord.ext import commands
import random
import magic8ball


class EightBall(commands.Cog):
    """
    Ask a Question, and CCU will answer it!

    Disclaimer: These answers are jokes and should be taken as jokes.
    For legal advice, talk to a lawyer. For general advice, don't take it from a bot.    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ateball", "8bl"])
    async def eightball(self, ctx, *, question):
        """
        Ask a question and get a response!

        Usage: [prefix]eightball <question>
        """
        embed = discord.Embed(
            title=f"Question by {ctx.author}:", description=question, color=5614335
        )

        embed.add_field(
            name="Answer:", value=random.choice(magic8ball.list), inline=False
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(EightBall(bot))
