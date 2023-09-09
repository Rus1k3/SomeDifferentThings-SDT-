from datetime import date
import math

def zefirka(m1,m2):
    return G * m1 * m2 // math.pow(R, 2)

dr = date(2005,5,30) # днюха
se = date(2023,9,1) # первое сентября
td = se - dr # вес в днях
m3 = td.days # вес в инт
m2 = m3 *1000
G = 6.6743 * math.pow(10, -11) #гравитационная постоянная
m1 = 5.97600 * math.pow(10, 24) #масса замли
R = 100000

print(zefirka(m1,m2))