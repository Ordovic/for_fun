from random import randint, choice
from time import sleep
def summ(a,b,num=20):
    breaked = False
    for i in range(num):
 
 
        # случайные настроения друг друга влияют друг на друга
        select_a = choice(['damage','bonus'])  # случайно выбираем настроение объекта а
        #print(select_a)
        select_b = choice(['damage','bonus'])  # случайно выбираем настроение объекта b
        #print(select_b)
 
        # само влияние на здоровье и энергию партнера
        if select_a == 'damage':
            b['health'] -= a['damage']
            b['energy'] -= round(a['damage']/5,2)
        else:
            b['health'] += a['bonus']
            b['energy'] += round(a['bonus']/5,2)
 
        # возвращаем здоровье на 100 в случае превышения 100  
        if b['health'] > 100:
            b['health'] = 100
 
 
        if select_b == 'damage':
            a['health'] -= b['damage']
            a['energy'] -= round(b['damage']/5,2)
        else:
            a['health'] += b['bonus']
            a['energy'] -= round(b['bonus']/5,2)
 
        # возвращаем здоровье на 100 в случае превышения 100      
        if a['health'] > 100:
            a['health'] = 100
 
        # старение и уменьшение энергии
        a['age'] += 1
        b['age'] += 1
        a['energy'] -= 1
        b['energy'] -= 1
 
 
        # здоровье с возрастом уменьшается
        a['health'] -= round(100/a['energy'],2)
        b['health'] -= round(100/b['energy'],2)
 
        if b['age'] == 100 or a['age'] == 100 or b['health'] <= 0 or a['health'] <= 0 or b['energy'] <= 0 or a['energy'] <= 0:
            if a['health'] <= 0 or b['health'] <= 0:
            	print('\n','Killed by partner',  '<-----', '\n')
            breaked = True
            break
            
    if i == num - 1 and not breaked:
        print('\n','Success!!!',  '<-----', '\n')
 
    print(name(a),a,name(b),b, sep = '\n')
 
 
def default():
    global Mary, Tom
    Mary = {'health': 95, 'damage': 7, 'bonus': 5, 'age': 25, 'energy': 70, 'experience': 24, 'bulletproof': 12}
    Tom = {'health': 92, 'damage': 9, 'bonus': 6, 'age': 27, 'energy': 58, 'experience': 32, 'bulletproof': 43}
 
default()
#summ(Mary,Tom)
 
def simulation(sims = 10,numer=27):
    for i in range(sims):
        print('simulation {0}'.format(i+1))
        summ(Mary,Tom, numer)
        print()
        default()
        sleep(1)
 



def name(*args):
    for arg in args:
        for loc in globals():
                res.append(loc)
    return res if len(res) > 1 else res[0]

simulation()
