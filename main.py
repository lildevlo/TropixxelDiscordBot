from discord.ext import commands
import discord

bot = commands.Bot(command_prefix=":-")


@bot.event
async def on_ready():
    print("Tropixeel Bot ready.")


@bot.command(name="ping")
async def pingpong(message):
    await message.channel.send("Pong")


@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()

    for each_message in messages:
        await each_message.delete()


@bot.command(name="members")
async def members(message):
    memberss = discord.approximate_member_count
    await message.channel.send(memberss)


bot.run("OTgxNTE1MTQ1MzU4NDkxNjc4.Gof7IQ.aOa59oZW4jje937MJ5pJHHMX0BVbZNdFA94AKo")
