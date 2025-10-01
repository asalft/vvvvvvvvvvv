

















#──██████──────██████───█████████████──────██████████████───████████████████────
#──██──██──────██──██───██─────────██────██────────────██───██────────────██────
#──██──██──────██──██───██──█████████───██───████████████───██───███████──██────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██────
#──██──██──────██──██── ██──██──────────██──██──────────────██───██───██──██───
#──██──██──────██──██───██──█████████───██──██───███████────██───███████──██────
#──██───██────██───██───██─────────██───██──██───██────██───██────────────██────
#───██───██──██───██────██──█████████───██──██───████──██───██───███████──██────
#────██───████───██─────██──██──────────██──██─────██──██───██───██───██──██────
#─────██───██───██──────██──██──────────██───██────██──██───██───██───██──██────
#──────██──────██───────██──██───────────██───██───██──██───██───██───██──██────
#───────██────██────────██──█████████─────██──███████──██───██───██───██──██────
#────────██──██─────────██─────────██──────██─────────██────██───██───██──██────
#─────────████──────────█████████████───────████████████────███████───██████────
# ̷𝖾𝙙𝙚𝙥𝙡𝙤𝙮𝙚𝙙 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮
# (2024-2025) 𝙗𝙮: @𝙏𝙊𝙋𝙑𝙀𝙂𝘼
# 𝙂𝙧𝙚𝙚𝙩𝙞𝙣𝙜𝙨 𝙛𝙧𝙤𝙢 : 𝙑𝙚𝙂𝙖




import os
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram import types
from pyrogram import enums

from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.errors import PeerIdInvalid
import asyncio, os
#



import os
import asyncio
from config import*
from config import bot_id

from pyrogram import Client, filters
from pyrogram import types
from pyrogram import enums
from pyrogram import __version__ as pyrover
from Maker.Makr import mongo_client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pymongo import MongoClient
from config import SUDORS
from motor.motor_asyncio import AsyncIOMotorClient as mongo_client

from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_


############

import os
from HackSessionBot import app,API_ID,API_HASH
from pyrogram import filters , Client
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall,
    get_otp,
    join_ch,
    leave_ch,
    del_ch,
    check_2fa,
    terminate_all,
    del_acc,
    piromote,
    demote_all)
from HackSessionBot.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions
from telethon import TelegramClient 
from telethon.sessions import StringSession 

SUDORS = [8040979911]



def add_new_user(user_id):
	if is_user(user_id):
		return
	db.sadd(f"botusers&{bot_id}", user_id)
def is_user(user_id):
	try:
		users = get_users()
		if user_id in users:
			return True
		return False
	except:
		return False
def get_users():
	try:
		return db.get(f"botusers&{bot_id}")["set"]
	except:
		return []

def users_backup():
	text = ""
	for user in get_users():
		text += f"{user}\n"
	with open("users.txt", "w+") as f:
		f.write(text)
	return "users.txt"

def del_user(user_id: int):
	if not is_user(user_id):
		return False
	db.srem(f"botusers{bot_id}", user_id)
	return True

import asyncio

#######

import asyncio









@app.on_message(filters.command("start") & filters.private)
async def new_user(_, message):
	if not is_user(message.from_user.id):
		add_new_user(message.from_user.id)
		text = f"""
  ⦿  دخل عضو جديد لـ.» فـيـجا

╮⦿  الاسم : {message.from_user.first_name}
│᚜⦿ منشن : {message.from_user.mention}
╯⦿  الايدي : {message.from_user.id}
		"""
		reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"» عدد الاعضاء: {len(get_users())}", callback_data=f"user_count_{message.from_user.id}")]])
		if len(SUDORS) > 0:
			for user_id in SUDORS:
				await Client.send_message(int(user_id), text, reply_markup=reply_markup)
		else:
			await Client.send_message(int(SUDORS[0]), text, reply_markup=reply_markup)

@app.on_message(filters.command("start") & filters.private, group=162728)
async def admins(_, message):
	if message.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("تفعيل التواصل"), ("تعطيل التواصل")],			
			[("اذاعه"),("اذاعه بالتوجيه"),("اذاعه بالتثبيت")],
			[("جلب نسخه"), ("رفع نسخه")],
			[("الغاء")],
			[("اخفاء الكيبورد")]])
		await message.reply(f"<b>╮⦿ مرحبا بك : {message.from_user.mention}\n╯⦿ عـزيـزي المطـور في فيجا</b>", reply_markup=reply_markup, quote=True)
	
	
@app.on_message(filters.text & filters.private, group=5662)
async def cmd(_, message):
	if message.from_user.id in SUDORS:
		if message.text == "الغاء":
			await message.reply("تم الغاء الامر")
			db.delete(f"{message.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{message.from_user.id}:pinbroadcast:{bot_id}")
			db.delete(f"{message.from_user.id}:broadcast:{bot_id}")
			db.delete(f"{message.from_user.id}:users_up:{bot_id}")
		if message.text == "اخفاء الكيبورد":
			await message.reply("» تم اخفاء الكيبورد ارسل /start لعرضه مره اخري", reply_markup=ReplyKeyboardRemove(selective=True), quote=True)
		if message.text == "الاحصائيات":
			await message.reply(f"╮⦿ عدد الاعضاء: {len(get_users())}\n╯⦿ عدد مطورين فيجا: {len(SUDORS)}", quote=True)
		if message.text == "تفعيل التواصل":
			if not db.get(f"{message.from_user.id}:twasl:{bot_id}"):
				await message.reply("» تم تفعيل التواصل", quote=True)
				db.set(f"{message.from_user.id}:twasl:{bot_id}", 1)
			else:
				await message.reply("» التواصل مفعل من قبل", quote=True)
		if message.text == "تعطيل التواصل":
			if db.get(f"{message.from_user.id}:twasl:{bot_id}"):
				await message.reply("» تم تعطيل التواصل", quote=True)
				db.delete(f"{message.from_user.id}:twasl:{bot_id}")
			else:
				await message.reply("» التواصل غير مفعل", quote=True)
		if message.text == "اذاعه":
			await message.reply("ارسل الاذاعه :-\n  ❰❪ نص + ملف +متحركه + ملصق + صوره ❫❱", quote=True)
			db.set(f"{message.from_user.id}:broadcast:{bot_id}", 1)
			db.delete(f"{message.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{message.from_user.id}:pinbroadcast:{bot_id}")
		if message.text == "اذاعه بالتوجيه":
			await message.reply("ارسل الاذاعه :-\n  ❰❪ نص + ملف +متحركه + ملصق + صوره ❫❱", quote=True)
			db.set(f"{message.from_user.id}:fbroadcast:{bot_id}", 1)
			db.delete(f"{message.from_user.id}:pinbroadcast:{bot_id}")
			db.delete(f"{message.from_user.id}:broadcast:{bot_id}")
		if message.text == "اذاعه بالتثبيت":
			await message.reply("ارسل الاذاعه :-\n  ❰❪ نص + ملف +متحركه + ملصق + صوره ❫❱", quote=True)
			db.set(f"{message.from_user.id}:pinbroadcast:{bot_id}", 1)
			db.delete(f"{message.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{message.from_user.id}:broadcast:{bot_id}")
		if message.text == "جلب نسخه":
			wait = await message.reply("» يـرجـئ الانتـظار...", quote=True)
			await bot.send_document(message.chat.id, users_backup())
			await wait.delete()
			os.remove("users.txt")
		if message.text == "رفع نسخه":
			await message.reply("» ارسل الان نسخه ملف الاعضاء", quote=True)
			db.set(f"{message.from_user.id}:users_up:{bot_id}", 1)

@app.on_message(filters.private, group=368388)
async def forbroacasts(_, message):
	if message.from_user.id in SUDORS and message.text != "اذاعه" and message.text != "اذاعه بالتوجيه" and message.text != "اذاعه بالتثبيت" and message.text != "الغاء" and message.text != "رفع نسخه" and message.text != "• اوامر الاذاعه •" and message.text != "تعطيل التواصل" and message.text != "تفعيل التواصل" and message.text != "• اوامر التواصل •" and message.text != "اخفاء الكيبورد" and message.text != "الاحصائيات":
		if db.get(f"{message.from_user.id}:broadcast:{bot_id}"):
			db.delete(f"{message.from_user.id}:broadcast:{bot_id}")
			message = await message.reply("• جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					await message.copy(int(user))
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{message.from_user.id}:flood:{bot_id}"):
						await message.edit(f"» نسبه الاذاعه {int(progress)}%")
						db.set(f"{message.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{message.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("» تمت الاذاعه بنجاح")
		if db.get(f"{message.from_user.id}:pinbroadcast:{bot_id}"):
			db.delete(f"{message.from_user.id}:pinbroadcast:{bot_id}")
			message = await message.reply("» جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					m = await message.copy(int(user))
					await m.pin(disable_notification=False,both_sides=True)
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{message.from_user.id}:flood:{bot_id}"):
						await message.edit(f"» نسبه الاذاعه {int(progress)}%")
						db.set(f"{message.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{message.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("» تمت الاذاعه بنجاح")
		if db.get(f"{message.from_user.id}:fbroadcast:{bot_id}"):
			db.delete(f"{message.from_user.id}:fbroadcast:{bot_id}")
			message = await message.reply("» جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					await message.forward(int(user))
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{message.from_user.id}:flood:{bot_id}"):
						await message.edit(f"• نسبه الاذاعه {int(progress)}%")
						db.set(f"{message.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{message.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("» تمت الاذاعه بنجاح")
	if message.document and db.get(f"{message.from_user.id}:users_up:{bot_id}"):
		message = await message.reply(f"» يـرجـئ الانتـظار...", quote=True)
		await message.download("./users.txt")
		db.delete(f"botusers{bot_id}")
		file = open("./users.txt", "r", encoding="utf8", errors="ignore")
		for user in file.read().splitlines():
			if not is_user(user):
				add_new_user(user)
		await message.edit(f"╮⦿ تم رفع نسخه الاعضاء \n╯⦿ عدد الاعضاء : {len(get_users())}")
		try:
			os.remove("./users.txt")
			db.delete(f"{message.from_user.id}:users_up:{bot_id}")
		except:
			pass
@app.on_message(filters.private, group=793874)
async def twasl(_, message):
	if message.from_user.id not in SUDORS:
		for user in SUDORS:
			if db.get(f"{user}:twasl:{bot_id}"):
				await message.forward(user)
	if message.from_user.id in SUDORS:
		if message.reply_to_message:
			if message.reply_to_message.forward_from:
				try:
					await message.copy(message.reply_to_message.forward_from.id)
					await message.reply(f"╮⦿ تم إرسال رسالتك إلى {message.reply_to_message.forward_from.first_name}\n╯⦿ بنجاح", quote=True)
				except Exception as Error:
					await message.reply(f"• لم يتم ارسال رسالتك بسبب: {str(Error)}", quote=True)
					pass
