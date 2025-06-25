import os
from discord.ext.commands import Bot
from discord import Intents

# from .classes.discordBot import DiscordBot
# from .commands import *


# bot = DiscordBot(token=__token, description="MidBot!", prefix='!')




class DiscordBot(Bot):

    def __init__(self, token: str, description: str = "", prefix: str = '!'):
        self.__token = token
        intent = Intents.default()
        super().__init__(command_prefix=prefix, intents=intent)
    
    def run(self):
        super().run(token=self.__token)


class BotRunner():

    @staticmethod
    def run_discord_bot():
        __token = os.environ.get('TOKEN')
        aliceBot = DiscordBot(token=__token, description="AliceBot!", prefix='!')
        aliceBot.run()
