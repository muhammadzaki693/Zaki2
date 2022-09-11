import os
from discord.ext import commands

bot = commands.Bot(
	command_prefix="z>",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 758298255389097984  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
	'cogs.cog_dev',
	'cogs.cog_comm'# Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot