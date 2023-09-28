from collections import Counter

pred = str(input('Введите что либо'))

def split(x):
    x = [char for char in x]
    return x

def sc_sim(x):
    x = split(x)
    count = Counter(x)
    return count

print(sc_sim(pred))