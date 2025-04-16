import discord
from discord.ext import commands

class CommandesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="bonjour_monde",
        aliases=['hw', 'hello_world'],
        description="Le Bot dit hello world",
        brief="Dit hello world",
        help="Encore plus d'aide",
        hidden=False
        )
    async def hello_word(self, context):
        await context.send("Hello, World !")

    @commands.hybrid_command(
        description="Lance un décompte a partir du nombre donné",
        brief="lance un décompte",
        help="Encore plus d'aide",
        hidden=False
    )
    async def decompte(self, context, delai: int):
        await context.send("Départ dans ...")
        for i in range(delai, 0, -1):
            await context.send(i)
        await context.send("C'est parti !")
    @commands.hybrid_command(
            name='boutique',
            description="Envoie vers la boutique du serveur",
            brief="La boutique",
            help="Encore plus d'aide",
            hidden=False
            )
    async def boutique(self, ctx):
        channel = discord.utils.get(ctx.guild.channels, name="🛒ﾉboutique")
        if channel:
            await ctx.send(f"Go to {channel.mention}")
        else:
            await ctx.send("Channel not found.")

    @commands.hybrid_command(
        name='instance',
        description="Vous dit si l'instance VRchat est ouvert",
        brief="Instance VRchat",
        help="Encore plus d'aide",
        hidden=False
        )
    async def instance(self, ctx):
        for channel in ctx.guild.voice_channels:
            if channel.name == "🌐ﾉInstance : Ouvert":
                await ctx.send("Instance : Ouvert")
            return
        await ctx.send("Instance : Fermé")
async def setup(bot):
    await bot.add_cog(CommandesCog(bot))