import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji = "꒰ <:InformationCategory:943427908691701771> ꒱"
        self.hidden = False
        self.description = "Includes Info Related Commands."

    @commands.command(description=f"Shows Server Info")
    @commands.guild_only()
    async def serverinfo(self, ctx):
        '''Shows Server Info'''
        server = ctx.guild
        roles = str(len(server.roles))
        emojis = str(len(server.emojis))
        channels = str(len(server.channels))

        embed = discord.Embed(title=server.name, colour=discord.Colour.blue())
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name="Server ID:", value=server.id, inline=False)
        embed.add_field(name="Total Users:", value=server.member_count, inline=True)
        embed.add_field(name="Server owner:", value=ctx.guild.owner, inline=True)
        embed.add_field(name="Server Region:", value=server.region, inline=True)
        embed.add_field(name="Verification Level:", value=server.verification_level, inline=True)
        embed.add_field(name="Role Count:", value=roles, inline=True)
        embed.add_field(name="Emoji Count:", value=emojis, inline=True)
        embed.add_field(name="Channel Count:", value=channels, inline=True)

        await ctx.reply(embed=embed)

    @commands.command(usage=f"`< user >`", description=f"Shows UserInfo.")
    @commands.guild_only()
    async def whois(self, ctx, *, user : discord.Member = None):
            '''Shows UserInfo.'''
            if user is None:
                user = ctx.author
            embed = discord.Embed(colour=discord.Colour.blue(), title=f"{user.name}")
            embed.set_footer(text=f"ID: {user.id}")
            embed.set_thumbnail(url=user.avatar_url_as(format="png"))
            embed.add_field(name="__**General information:**__", value=f"**Discord Name:** {user}\n"f"**Account created:** {user.created_at.__format__('%A %d %B %Y at %H:%M')}\n")
            embed.add_field(name="__**Server-related information:**__", value=f"**Nickname:** {user.nick}\n"f"**Joined server:** {user.joined_at.__format__('%A %d %B %Y at %H:%M')}\n"f"**Roles:** {' '.join([r.mention for r in user.roles[1:]])}")
            return await ctx.reply(embed=embed)

    @commands.command(description=f"Shows Server Members.")
    @commands.guild_only()
    async def users(self, ctx):
        '''Shows Server Members'''
        server = ctx.guild
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name="Total Server Members:", value=server.member_count, inline=True)
        return await ctx.reply(embed=embed)



def setup(bot):
    bot.add_cog(Info(bot))