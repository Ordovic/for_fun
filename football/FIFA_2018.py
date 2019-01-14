import os
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
import operator
import pymorphy2
morph = pymorphy2.MorphAnalyzer()


sklonenia = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']

os.chdir('')
# print(os.getcwd())

text_file = open('FIFA.txt', 'r', encoding='utf-8')
spisok = text_file.read().lower().split()
spisok = sorted(spisok)
# print(spisok)
# редаетируем отсортированный список и убераем от туда спец символы;
for n, b in enumerate(spisok):
    spisok[n] = spisok[n].strip('. , : ; ! ? @ -')
    if spisok[n].isnumeric():
        spisok[n] = ''
    if not str(spisok[n]).isalpha():
        spisok[n] = ''
# в новый список добавляем отредоктированный список без пустых строк;
spisok_1 = []
for h, k in enumerate(spisok):
    if k != '':
        spisok_1.append(k)
# print(spisok_1)

pars = {}
# загружаем уже СОЗДАННЫЙ exel файл;
pars_xlsx = load_workbook('FIFA.xlsx')
sheet = pars_xlsx['Sheet']
# добовляем в словарь значение при условии отсутствия их;
for football in spisok_1:
    if not football in pars:
        pars[football] = 0
    pars[football] += 1

find = input('введите слово которое нужно найти: ')
sklon = []
sklon_1 = morph.parse(find)[0]
for i in range(len(sklonenia)):
    sklon.append(sklon_1.inflect({sklonenia[i]}).word)
# print(sklon)


# сортировка словаря в новую переменную;
sorted_pars = dict(
    sorted(pars.items(), key=operator.itemgetter(1), reverse=True))
# print(sorted_pars)

for i, a in enumerate(range(len(sorted_pars))):
    sheet['A' + str(2 + a)] = (list(sorted_pars.keys())[i])
    sheet['B' + str(2 + a)] = (list(sorted_pars.values())[i])

for l in range(6):
    sheet['D' + str(2 + l)] = sklon[(int(l))]
    sheet['E' + str(2 + l)] = sorted_pars.get(str(sklon[int(l)]))

print(sheet['A2'].value)
pars_xlsx.save('FIFA.xlsx')

url = 'https://www.znak.com/2018-07-15/franciya_vyigrala_chempionat_mira_po_futbolu'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
football = soup.prettify()
# print(football)
a = football.find('<section class="footer">')
b = football.find('<p>')
v = football[b:a]
m = v[:v.find('<a')] + v[v.find('</a>') + 4:]
finish = m.replace('<p>', '').replace('</p>', '')
print(finish)

# статья еще с двух сайтов и сравнение двух статей график с числами;

'''
print(soup.find_all('p')[1].get_text())
for i, m in enumerate(soup.find_all('p')):
    print(m.get_text(), i)
'''


























# падежи и отсортировать по убыванию;
