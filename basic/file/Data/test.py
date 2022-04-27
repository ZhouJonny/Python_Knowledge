import random

with open('temperature.txt', 'w') as file:
    for i in range(100):
        temperature = random.uniform(36.0, 39.9)
        file.write(f'病人{i+1} {temperature:.1f}\n')