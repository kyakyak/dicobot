import discord
from discord.ext import commands

import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
html = requests.get("http://gsm.gen.hs.kr/xboard/board.php?tbnum=42", headers=headers).text
bsObject = BeautifulSoup(html, "lxml")

strB = ""
strL = ""
strD = ""

check = 000  # 조/중/석

if bsObject.find(attrs={"class": "today"}).find(attrs={"class": "con1"}) == None:
    strB = "조식이 없습니다."
    check += 100

if bsObject.find(attrs={"class": "today"}).find(attrs={"class": "con2 first"}) == None:
    strL = "중식이 없습니다."
    check += 10

if bsObject.find(attrs={"class": "today"}).find(attrs={"class": "con3"}) == None:
    strD = "석식이 없습니다."
    check += 1

if check / 100 == 1.0:
    Breakfast = bsObject.find(attrs={"class": "today"}).find(attrs={"class": "con1"}).find(attrs={"class": "content"})

    for tag in Breakfast:
        strB = strB + tag.get_text()

if check / 100 == 1.0:
    Lunch = bsObject.find(attrs={"class": "today"}).find(attrs={"class": "con2 first"}).find(attrs={"class": "content"})

    for tag in Lunch:
        strL = strL + tag.get_text()

if check / 100 == 1.0:
    Dinner = bsObject.find(attrs={"class": "today"}).find(attrs={"class": "con3"}).find(attrs={"class": "content"})

    for tag in Dinner:
        strD = strD + tag.get_text()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="급식 탐색"))
    print("봇이 시작되었습니다.")


@bot.command()
async def 급식(ctx):
    await ctx.send("```-조식-\n\n" + strB + "\n\n-중식-\n\n" + strL + "\n\n-석식-\n\n" + strD + "```")


@bot.command()
async def 아침(ctx):
    await ctx.send("```-조식-\n\n" + strB + "```")


@bot.command()
async def 점심(ctx):
    await ctx.send("```-중식-\n\n" + strL + "```")


@bot.command()
async def 저녁(ctx):
    await ctx.send("```-석식-\n\n" + strD + "```")


@bot.command()
async def 명령어(ctx):
    await ctx.send("```명령어 종류\n\n급식\n아침\n점심\n저녁\n명령어```")


@bot.event
async def on_message(message):
    content = message.content
    author = message.author
    channel = message.channel

    if author.bot:
        return None

    elif content.startswith('급식'):
        await channel.send("```-조식-\n\n" + strB + "\n\n-중식-\n\n" + strL + "\n\n-석식-\n\n" + strD + "```")

    elif content.startswith('아침'):
        await channel.send("```-조식-\n\n" + strB + "```")

    elif content.startswith('점심'):
        await channel.send("```-중식-\n\n" + strL + "```")

    elif content.startswith('저녁'):
        await channel.send("```-석식-\n\n" + strD + "```")

bot.run('MTEyMjcyMTgzMjc5ODI2OTUyMg.GqLGSL.1vDSSjtBGy5w-3630NSkE9ovTzI8gt9TJCuNPo')
