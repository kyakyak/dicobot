import discord
from discord.ext import commands

import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
html = requests.get("http://gsm.gen.hs.kr/xboard/board.php?tbnum=42",headers=headers).text
bsObject = BeautifulSoup(html,"lxml")

strB = ""
strL = ""
strD = ""

Breakfast = bsObject.find(attrs={"class":"today"}).find(attrs={"class":"con1"}).find(attrs={"class":"content"})
Lunch = bsObject.find(attrs={"class":"today"}).find(attrs={"class":"con2 first"}).find(attrs={"class":"content"})
Dinner = bsObject.find(attrs={"class":"today"}).find(attrs={"class":"con3"}).find(attrs={"class":"content"})

for tag in Breakfast:
    strB = strB + tag.get_text()

for tag in Lunch:
    strL = strL + tag.get_text()

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

    elif content.startswith('엄'):
        await channel.send('준식')

    elif content.startswith('와'):
        await channel.send('```샌즈! 아시는구나! 그거 겁나게 어.렵.습.니.다```')

    elif content.startswith('?'):
        await channel.send('왜 뭐 왜 어쩌라구')

    elif content.startswith('급식'):
        await channel.send("```-조식-\n\n" + strB + "\n\n-중식-\n\n" + strL + "\n\n-석식-\n\n" + strD + "```")

    elif content.startswith('아침'):
        await channel.send("```-조식-\n\n" + strB + "```")

    elif content.startswith('점심'):
        await channel.send("```-중식-\n\n" + strL + "```")

    elif content.startswith('저녁'):
        await channel.send("```-석식-\n\n" + strD + "```")

    elif content.startswith('명령어'):
        await channel.send("```명령어 종류\n\n급식\n아침\n점심\n저녁\n그 외 나머지는 알아서 찾아 보시오```")

    elif content.startswith('그 외 나머지는 알아서 찾아 보시오'):
        await channel.send("```원하시는 것 같길래 추가 해드렸습니다 짜잔~!```")

    elif content.startswith('이스터에그'):
        await channel.send("```흠...이스터에그라...만들기 어렵네요```")

    elif content.startswith('ㅋ'):
        await channel.send("```ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ```")

    elif content.startswith('ㅎ'):
        await channel.send("```ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ```")

    elif content.startswith('ㅠ'):
        await channel.send("```ㅠㅠㅠ```")

    elif content.startswith('흠'):
        await channel.send("```고민이 있으신가요?```")

    elif content.startswith('로보틱스'):
        await channel.send("```아주 좋습니다```")

    elif content.startswith('제작자'):
        await channel.send("```이 이스터에그를 추가하고 있는 제작자의 심정을 생각 해 보셨나요?```")

    elif content.startswith('뭐'):
        await channel.send("```아뇨 아무것도 하지 않았습니다```")

    elif content.startswith('ㄹㅇㅋㅋ'):
        await channel.send("```ㄹㅇㅋㅋ```")

    elif content.startswith('참고'):
        await channel.send("```이스터에그들은 실시간으로 추가 되고 있습니다```")

    elif content.startswith('실시간'):
        await channel.send("```실시간으로 모든 작업을 하기에는...```")

    elif content.startswith('학진봇'):
        await channel.send("```일 하기 싫습니다```")

    elif content.startswith('gsm 제 1 법칙'):
        await channel.send("```컴퓨터를 켜놓은 상태로 자리를 비우지 않는다.g```")

bot.run('MTEyMjcyMTgzMjc5ODI2OTUyMg.G8IrU1.FfOqK0zOkcE0K7lPpTWS_PysrBoda7ytIrgFD4')