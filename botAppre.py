import discord
from discord.ext import commands


bot = commands.Bot(command_prefix= "/", description= "Bot de test .py")


@bot.event
async def on_ready():
    print("Ready!")


@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDesc = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur {serverName} contient {numberOfPerson} personnes. \n La description du serveur {serverDesc}. \n Ce serveur contient {numberOfTextChannels} salons textuels ainsi que {numberOfVoiceChannels} channel vocaux."
	await ctx.send(message)


@bot.command()
async def say(ctx, *text):
	await ctx.send(" ".join(text))


@bot.command()
async def chinese(ctx, *textchine):
	chineseChar = "凡乃ㄈ刀モ下G什ﾉﾌに乚州几ロ尸Q尺らイ凵レ山ㄨㄚ乙"
	chineseText = []
	for word in textchine:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
			chineseText.append(" ")
	await ctx.send("".join(chineseText))


@bot.command()
async def botinfo(ctx):
	message = "`BotAppren est un bot crée par 7єɱρєꜱʈ.sk#0417. \nLanguage de programation: Phyton. \nDescription: botAppren est un robot déstiné a l'apprentissage du py pour 7єɱρєꜱʈ.sk#0417`"
	await ctx.send(message)


@bot.command()
async def clear(ctx, number : int):
	messages = await ctx.channel.history(limit = number + 1).flatten()
	for message in messages:
		await message.delete()


@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick du serveur pour {reason}")


@bot.command()
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été banni pour {reason}")


@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} a été debanni")
			return
	await ctx.send(f"L'utilisateur {user} ne fait pas parti de la liste des malfrats...")


@bot.command()
async def ip(ctx):
	await ctx.send("L'ip du serveur est **play.naosya.eu**")


@bot.command()
async def codesource(ctx):
	await ctx.send("https://hatebin.com/fddssbhict")


bot.run("Nzk0NjY0NDkwOTg1MDYyNDQw.X--G-g.dLO-y7bDLB5iMakoWmxjOKc3kGA")