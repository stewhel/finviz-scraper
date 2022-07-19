import requests
from datetime import datetime, timedelta
import sched, time
import yagmail
from discord.ext import commands
import asyncio
import sys

import sys
sys.path.append('c:/users/steph/appdata/local/programs/python/python39/lib/site-packages')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append('C:/Users/steph/anaconda3/pkgs/beautifulsoup4-4.9.3-pyhb0f4dca_0/site-packages')
import bs4
from bs4 import BeautifulSoup

def scrape():

    print("Starting Active Stocks Scrape....")

    body = "Today's Active Stocks: \n"

    url = 'https://finviz.com/screener.ashx?v=111&f=sh_curvol_o1000,sh_price_o1,sh_relvol_o10&o=-change'

    driver = webdriver.Chrome(executable_path = r'c:/users/steph/downloads/chromedriver_win32/chromedriver.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    data = soup.find("div", {"id": "screener-content"})
    data = data.findChildren('table')
    data = data[0]
    data = data.findChildren('table')
    data = data[2]
    data = data.findChildren(['tbody', 'tr'])

    for i in data[2:]:
        cells = i.findChildren('td')
        body += " \n"
        for cell in cells[1], cells[9]:
            body += str(cell.text) +  " "

    body += "\n * https://finviz.com/screener.ashx?v=111&f=sh_curvol_o1000,sh_price_o1,sh_relvol_o10&o=-change"

    print("Scrape finished!")

    bot = commands.Bot(command_prefix='!')

    TOKEN = '{ADD YOUR DISCORD BOT TOKEN HERE}'


    async def post():
        await bot.wait_until_ready()
        msg_sent = False

        if not msg_sent:
            channel = bot.get_channel('{CHANNEL TO SEND MESSAGE IN}')
            await channel.send(body)
            msg_sent = True
            sys.exit()

    bot.loop.create_task(post())
    bot.run(TOKEN)

scrape()
