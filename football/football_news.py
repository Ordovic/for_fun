import os
import requests
import openpyxl
from bs4 import BeautifulSoup
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
sklonenia = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']

#os.chdir('')
# print(os.getcwd())
arg = openpyxl.Workbook()
sheet = arg.active


def extracting(a):
    url = a
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    football = soup.prettify()
    # print(football)
    data = []
    table = soup.find('table', attrs={'class': 'standard'})
    #print(table)
    rows = table.find_all('tr')
    #print(rows)
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

fifa_2010 = 'https://ru.wikipedia.org/wiki/Чемпионат_мира_по_футболу_2010'
class_2010 = ['standard', ]
print(extracting(fifa_2010))