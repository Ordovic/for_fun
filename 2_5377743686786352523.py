#itProger.com
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой
import datetime
'''
from tkinter import *

window = Tk()
holst = Canvas(window, width = 800, height = 600)
window.title('Контроль курса валюты')
holst.pack()'''


koefic = 'https://www.flashscore.ru/match/fghzIVzJ/#match-summary'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

full_page = requests.get(koefic, headers=headers)


soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "odds-wrap up"})
print(convert)

 
'''       return convert[0].text

'''
