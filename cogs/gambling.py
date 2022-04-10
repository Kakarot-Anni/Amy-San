import discord
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
import os
from imgurpython import ImgurClient
from random import choice , randint
import giphy_client
from giphy_client.rest import ApiException

class Gambling(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.emoji = "꒰ <a:GamblingCategory:943427904648388618> ꒱"
        self.hidden = True
        self.description = "Includes Gambling Related Commands."

     
def setup(bot):
    bot.add_cog(Gambling(bot))