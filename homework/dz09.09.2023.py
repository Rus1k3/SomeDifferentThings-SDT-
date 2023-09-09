import math

G = 6.6743 * math.pow(10, -11) #гравитационная постоянная

m1 = 5.97600 * math.pow(10, 24) #масса замли

mas = float(input('введите массу планеты например луны -'))
os = int(input('введите на что умножается в степени - '))
st = int(input('введите показатель степени - '))

m2 = mas * math.pow(os, st)

R = int(input('введите расстояние от планеты до земли(в метрах) - '))

def fyz_fync(m1,m2):
    return G * m1 * m2 // math.pow(R, 2)


print(fyz_fync(m1, m2))
