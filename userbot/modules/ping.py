# Copyright (C) 2019 The Raphielscape Company LLC.
# RAM-UBOT MINTA
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, StartTime, REPO_NAME, DEVG, BOT_VER
from userbot.events import register

gesss = [
    "Eh ada Owner keren",
    "Hadir ganteng 😍",
    "Hi Tuan, kemana sj? 🤗",
    "Hadir kak 😉",
    "Hadir bang 😁",
    "Hadir bang maap telat 🥺",
    "Saya slalu ada buat Tuan Owner🥵",
    "Jangan kemana mana lagi ya bang",
    "Pas banget bang, aku lagi kangen",
    "Bang owner on juga akhirnya🥵",
]

brb = [
    "Bang owner mau off.",
    "Jangan off dong bang.",
    "Bang, mau kemana?",
    "Jangan lama lama bang",
    "Siap bang.",
    "Yah udah off aja bang.",
    "Off lagi, mau ngewe ya?",
    "Bang developer, lagi ange kah? ",
    "Jangan lupa makan bang.",
    "Yah pasti mao bucin ni.",
    "Jangan off terus lah bang.",
    "Mau nonton bokep kah?",
    "Bang Ganteng telah off.",
]

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVG, pattern=r"^gesss$")
async def _(landak):
    await landak.reply(random.choice(gesss))


@register(incoming=True, from_users=1826643972, pattern=r"^brb$")
async def _(landak):
    await landak.reply(random.choice(brb))


@register(outgoing=True, pattern="^Ping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Mengecek Sinyal...**")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    await asyncio.sleep(2)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**🌟𝗥𝗔𝗠-𝗨𝗕𝗢𝗧🌟**\n"
        f"** ➠  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ➠  Bᴏᴛᴠᴇʀ  :** "
        f"`{BOT_VER}` \n"
        f"** ➠  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ➠  Oᴡɴᴇʀ   :** `{ALIVE_NAME}` \n" % (duration)
    )

@register(outgoing=True, pattern="^.ping$")
@register(incoming=True, from_users=1779447750, pattern=r"^\.cpi$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("PONG!!")
    await asyncio.sleep(2)
    await pong.edit(f"{REPO_NAME}")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"{REPO_NAME}!!\n"
                    f"OWNER : {ALIVE_NAME}\n `%sms`\n"
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...✨`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   f"✧ **BOT:** {REPO_NAME}")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    await pong.edit("`Pong...........🐎`")
    await pong.edit("`Pong..........🐎.`")
    await pong.edit("`Pong.........🐎..`")
    await pong.edit("`Pong........🐎...`")
    await pong.edit("`Pong.......🐎....`")
    await pong.edit("`Pong......🐎.....`")
    await pong.edit("`Pong.....🐎......`")
    await pong.edit("`Pong....🐎.......`")
    await pong.edit("`Pong...🐎........`")
    await pong.edit("`Pong..🐎.........`")
    await pong.edit("`Pong.🐎..........`")
    await pong.edit("`Pong🐎...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**⚡Oᴡɴᴇʀ : {ALIVE_NAME}**\n📗 `%sms`" % (duration))


CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` or `Ping`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pong`\
         \n↳ : Sama Seperti Perintah Ping."})
