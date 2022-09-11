import discord
from discord.ext import commands

class Comm(commands.Cog,name="commands"):
	'''these are commands for member only'''
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="say")
	async def say(self, ctx, *, message):
		await ctx.send(message)
		if message is None:
			await ctx.send("give me something to say")

	@commands.command(name="ping")
	async def ping(self, ctx):
		await ctx.send(f"ping {round(self.bot.latency * 1000)}ms")

def setup(bot):
	bot.add_cog(Comm(bot))