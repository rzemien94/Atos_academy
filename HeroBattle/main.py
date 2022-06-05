import random

from Batman import Batman
from SpiderMan import SpiderMan

batman = Batman('batman', 3, 100, 100, 100, "batmobil")
spiderman = SpiderMan('spiderman', 3, 100, 100, 100, 6)

while True:
    if batman.health <= 0:
        print('Spiderman won the battle!')
        break
    if spiderman.health <= 0:
        print('Batman won the battle!')
        break
    i = random.randint(0, 1)
    if i == 0:
        if spiderman.spiders > 0:
            spiderman.attack_by_spiders(batman)
            print(f"{spiderman.name} attack {batman.name} with special attack, {batman.name} health: {batman.health}")
            continue
        spiderman.attack(batman)
        print(f"{spiderman.name} attack {batman.name} with normal attack, {batman.name} health: {batman.health}")
        continue
    batman.attack(spiderman)
    print(f"{batman.name} attack {spiderman.name} with normal attack, {spiderman.name} health: {spiderman.health}")
    continue

print('The game is over')
