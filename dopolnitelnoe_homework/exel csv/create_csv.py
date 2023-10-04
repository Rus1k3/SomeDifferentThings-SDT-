import csv
import random


numbers = [random.randint(1, 100) for x in range(1000)]


with open('numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    for i, num in enumerate(numbers):
        writer.writerow([i, num])