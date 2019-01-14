import requests
from bs4 import BeautifulSoup
import openpyxl
import os

# print(os.getcwd())


def extracting():
    url = 'http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    baseball = soup.prettify()
    # print(baseball)
    data = []
    table = soup.find('table', attrs={'class': 'wikitable'})
    rows = table.find_all('tr')
    # print(rows)
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data


def saving(m):
    arg = openpyxl.Workbook()
    sheet = arg.active
    for x in m:
        sheet.append(x)
    arg.save('baseball.xlsx')


def table_title():
    arg = openpyxl.load_workbook('baseball.xlsx')
    sheet = arg.active
    a = ['Name', 'Team', 'Position', 'Height', 'Weight', 'Age']
    for i, m in enumerate(a):
        sheet[chr(65 + i) + '1'] = m
    arg.save('baseball.xlsx')


extracting()
saving(extracting())
table_title()
