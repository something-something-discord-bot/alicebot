from dotenv import load_dotenv
from src.runbot import BotRunner


load_dotenv('.env.example')

if __name__ == '__main__':
    try:
        BotRunner.run_discord_bot()
    finally:
        print('exitted the program')
