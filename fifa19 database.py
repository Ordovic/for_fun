from pandas import *
from tkinter import *
from tkinter.ttk import *
from time import sleep
from random import *
import random
#Библиотеки загрузки фото из интернета
import requests
from io import BytesIO
from urllib.request import urlopen

from PIL import *
from PIL import ImageTk,Image

data=read_csv(r'C:\Users\тест\Desktop\fifa19.csv')

#Переменные, хранящие параметры отбора:
names=set(data['Name'])
position=set(data['Position'])
team=sorted(list(set(data['Club'].dropna())))
nationality=set(data['Nationality'])
age=set(data['Age'])

#Окно Tkinter:
window = Tk()
window.geometry('800x600')
holst = Canvas(window, width = 800, height = 600)
label = Label(window, text='База данных игроков', font =('Arial',18), background = 'LIGHTBLUE')
label.place(relx=0.4,rely=0.05)
label = Label(window, text='*Данные взяты из базы FIFA19 за 2019год!', font =('Arial',9), background = 'LIGHTBLUE')
label.place(relx=0.4,rely=0.95)


#Имя игрока:
name=StringVar()
namelabel = Entry(window, width=15)
namelabel.place(relx=0.2, rely=0.05)

#Заполняем список игроков СЛЕВА
def IncludeChoosePlayer():
    name_boxL.delete(0,END)
    global names
    if name.get()!='':
        name1=[data['Name'][i] for i in range(len(data)) if data['Name'][i]==name.get()]
        names=names.intersection(name1)
    #print(tem.get(),pos.get(),'Agemin ',min_.get(),'Agemax ',max_.get(),'Name ',name.get(),'National',nat.get(),sep='\n')
    if tem.get()!='':
        club=[data['Name'][i] for i in range(len(data)) if data['Club'][i]==tem.get()]
        names=names.intersection(set(club))
        #print(names)
    if pos.get()!='':
        Posi=[data['Name'][i] for i in range(len(data)) if data['Position'][i]==pos.get()]
        names=names.intersection(set(Posi))
        #print(names)
    if min_.get()!=0:
        Age_min=[data['Name'][i] for i in range(len(data)) if data['Age'][i]>=min_.get()]
        names=names.intersection(set(Age_min))
        #print(names)
    if max_.get()!=0:
        Age_max=[data['Name'][i] for i in range(len(data)) if data['Age'][i]<=max_.get()]
        names=names.intersection(set(Age_max))
        #print(names)
    if nat.get()!='':
        Nationality=[data['Name'][i] for i in range(len(data)) if data['Nationality'][i]==nat.get()]
        names=names.intersection(set(Nationality))
        #print(names)
    for play_name in names:
        name_boxL.insert(END, play_name)
        
    #Заполняем поля возраста:  
    name_label6x.delete(0,END)
    name_label6c.delete(0,END)
    name_label6x.insert(END,min_.get())
    name_label6c.insert(END,max_.get())
    #Возращаем значение names к начальному:
    names=set(data['Name'])

#Выбираем игроков из списка СЛЕВА
def LeftChoosePlayer(event):       
    d=name_boxL.get(ACTIVE)
    correct_photo=''
    photo=[data['Photo'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    correct_photo=photo[0].replace('org','com').replace('4/19/','')
    a=correct_photo[-10:-4]
    b=correct_photo[-10:-7]
    c=correct_photo[-7:-4]
    v=b+'/'+c
    correct_photo2=correct_photo.replace(a,v)
    y=correct_photo2[-4:]
    u='/20_120.png'
    correct_photo_finish=correct_photo2.replace(y,u)
    print(correct_photo_finish)
    url=correct_photo_finish
    response = requests.get(url, timeout=10)
    image = Image.open(BytesIO(response.content))
    image = image.resize((130, 150),Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    labela.config(image=image, text='')
    labela.image = image  
    
    namelabel.delete(0,END)
    namelabel.insert(END, name_boxL.get(ACTIVE)) 
    print(d)
    ID=[data['ID'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    print(ID)
    id_label.delete(0,END)
    id_label.insert(END,('ID:',ID))
    cost_label.delete(0,END)
    cost=[data['Release Clause'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    cost_label.insert(END,cost)
    posit=[data['Position'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    poslabel.delete(0,END)
    poslabel.insert(END,posit)
    Club=[data['Club'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    temlabel.delete(0,END)
    temlabel.insert(END,Club)
    nat=[data['Nationality'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    natlabel.delete(0,END)
    natlabel.insert(END,nat)
    age=[data['Age'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    agelabel.delete(0,END)
    agelabel.insert(END,('Age:',age))
    rat=[data['Overall'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    ratlabel.delete(0,END)
    ratlabel.insert(END,(rat))
    pot_label.delete(0,END)
    pot=[data['Potential'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    pot_label.insert(END,('Potential-',pot))    

    
#Функция выбора игрока из правого списка:
def RightChoosePlayer(event):
    d=name_box.get(ACTIVE)
    correct_photo=''
    photo=[data['Photo'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    correct_photo=photo[0].replace('org','com').replace('4/19/','')
    a=correct_photo[-10:-4]
    b=correct_photo[-10:-7]
    c=correct_photo[-7:-4]
    d=b+'/'+c
    correct_photo2=correct_photo.replace(a,d)
    y=correct_photo2[-4:]
    u='/20_120.png'
    correct_photo_finish=correct_photo2.replace(y,u)
    print(correct_photo_finish)
    url=correct_photo_finish
    response = requests.get(url, timeout=10)
    image = Image.open(BytesIO(response.content))
    image = image.resize((130, 150),Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    labela.config(image=image, text='')
    labela.image = image  
    
    d=name_box.get(ACTIVE)
    namelabel.delete(0,END)
    namelabel.insert(END,name_box.get(ACTIVE)) 
    ID=[data['ID'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    id_label.delete(0,END)
    id_label.insert(END,('ID:',ID))
    cost_label.delete(0,END)
    cost=[data['Release Clause'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    cost_label.insert(END,cost)
    posit=[data['Position'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    poslabel.delete(0,END)
    poslabel.insert(END,posit)
    Club=[data['Club'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    temlabel.delete(0,END)
    temlabel.insert(END,Club)
    nat=[data['Nationality'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    natlabel.delete(0,END)
    natlabel.insert(END,nat)
    age=[data['Age'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    agelabel.delete(0,END)
    agelabel.insert(END,('Age:',age))
    rat=[data['Overall'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    ratlabel.delete(0,END)
    ratlabel.insert(END,(rat))
    pot_label.delete(0,END)
    pot=[data['Potential'][t] for t in range(len(data)) if data['Name'][t] == str(d)]
    pot_label.insert(END,('Potential-',pot))    


id_label = Entry(window, width=10)
id_label.place(relx=0.2, rely=0.09)    
cost_label = Entry(window, width=15)
cost_label.place(relx=0.2, rely=0.3) 
pot_label = Entry(window, width=15)
pot_label.place(relx=0.2, rely=0.25) 
    
name_label = Entry(window, font =('Arial',8),textvariable=name)
name_label.place(relx=0.4,rely=0.2, width=250, height = 30)
name_label2 = Label(window, text="Player's name")
name_label2.place(relx=0.4,rely=0.16)

#Comboboxes Позиции и Клуба игрока:
pos=StringVar()
ratlabel = Entry(window, width=4, font=('Arial',20),justify=CENTER,background="Green")
ratlabel.place(relx=0.065, rely=0.23)
poslabel = Entry(window, width=6)
poslabel.place(relx=0.05, rely=0.3)
agelabel = Entry(window, width=8)
agelabel.place(relx=0.1, rely=0.3)

name_label04 = Combobox(window, font =('Arial',10),textvariable=pos)
name_label04['values'] = list(position)
name_label04.place(relx=0.4,rely=0.3, width=250, height = 30)
name_label4 = Label(window, text="Player's Position")
name_label4.place(relx=0.4,rely=0.26)

tem=StringVar()
temlabel = Entry(window, width=15)
temlabel.place(relx=0.2, rely=0.2)

name_label05 = Combobox(window, font =('Arial',10),textvariable=tem)
name_label05['values'] = list(team)
name_label05.place(relx=0.4,rely=0.4, width=250, height = 30)
name_label5 = Label(window, text="Player's Team")
name_label5.place(relx=0.4,rely=0.36)


#Scales Возраста:
min_=IntVar()
max_=IntVar()
name_label6x = Entry(window, width=5)
name_label6x.place(relx=0.75,rely=0.5)
name_label6c = Entry(window, width=5)
name_label6c.place(relx=0.75,rely=0.6)

name_label06a = Scale(window, orient = 'horizontal', 
 from_=list(age)[0], to=list(age)[-1], variable=min_)
name_label06a.place(relx=0.4,rely=0.5, width=250, height = 30)
name_label06b = Scale(window, orient = 'horizontal', 
 from_=list(age)[0], to=list(age)[-1], variable=max_)
name_label06b.place(relx=0.4,rely=0.6, width=250, height = 30)
name_label6 = Label(window, text="Player's Age MIN(16) and MAX(45)")
name_label6.place(relx=0.4,rely=0.46)


#Combobox национальности:
nat=StringVar()
natlabel = Entry(window, width=15)
natlabel.place(relx=0.2, rely=0.15)

name_label04 = Combobox(window, font =('Arial',10),textvariable=nat)
name_label04['values'] = list(nationality)
name_label04.place(relx=0.4,rely=0.7, width=250, height = 30)
name_label4 = Label(window, text="Player's Nationality")
name_label4.place(relx=0.4,rely=0.66)


#Progressbar заполнения параметров поиска:
name_label07 = Progressbar(window, length=300)
val=0
def count_progressbar():
    val=0
    if name.get() !='':
        val+=+25
    if nat.get() !='':
        val+=+25
    if tem.get() !='':
        val+=+25
    if pos.get() !='':
        val+=+25
    name_label07['value'] = val
    name_label07.place(relx=0.4,rely=0.8, width=250, height = 30)

#Начальное расположение поля progressbar:
name_label07.place(relx=0.4,rely=0.8, width=250, height = 30)


#Listbox Right:
name_box = Listbox()
name_box.pack(side = RIGHT, fill= Y)
scrollbar = Scrollbar(command=name_box.yview) 
scrollbar.pack(side=RIGHT, fill= Y)
name_box.config(yscrollcommand=scrollbar.set)
leftLabel = Label(window, text='Активация 2х нажатие левой кнопки->>>', font =('Arial',8))
leftLabel.place(relx=0.55,rely=0.02)
for i in data['Name']: 
    name_box.insert(END, i) 

#Listbox LEFT:
name_boxL = Listbox()
name_boxL.place(x=15, y=285, width=200, height = 300)
leftLabel = Label(window, text='Активация 2х нажатие правой кнопки', font =('Arial',8))
leftLabel.place(relx=0.02,rely=0.44)

#Поле под фото игрока:
labela = Label(window, font =('Arial',18),relief=RIDGE)
labela.place(relx=0.02,rely=0.02, width=130, height = 120)


#Button "Search":
button = Button(text='Search', command=lambda:[IncludeChoosePlayer(),count_progressbar()])
button.place(relx=0.5,rely=0.9)
#Настройка кнопок активации:
window.bind('<Double-Button-1>', RightChoosePlayer)
window.bind('<Double-Button-3>', LeftChoosePlayer)
window.mainloop()