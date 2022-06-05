class Hero:
    def __init__(self, name, demage, health, mana, money):
        self.name = name
        self.demage = demage
        self.health = health
        self.mana = mana
        self.money = money

    def rest(self):
        self.mana += 20

    def atack(self):
        self.health -= 20

    def rob(self):
        self.money = 0


class Batman(Hero):
    def increase_demage(self, i):
        self.demage += i


batman = Batman('batman', 100, 100, 100, 100)
print(batman.name, batman.mana, batman.money, batman.health, batman.demage)
batman.increase_demage(50)
print(batman.name, batman.mana, batman.money, batman.health, batman.demage)

hero1 = Hero('hero1', 100, 100, 100, 100)
hero2 = Hero('hero2', 50, 50, 50, 50)

print(hero1.name, hero1.mana, hero1.money, hero1.health, hero1.demage)
print(hero2.name, hero2.mana, hero2.money, hero2.health, hero2.demage)
hero1.rest()
hero2.atack()
hero2.rob()
print(hero1.name, hero1.mana, hero1.money, hero1.health, hero1.demage)
print(hero2.name, hero2.mana, hero2.money, hero2.health, hero2.demage)

batman = Batman('batman', 100, 100, 100, 100)
print(batman.name, batman.mana, batman.money, batman.health, batman.demage)
batman.increase_demage(50)
print(batman.name, batman.mana, batman.money, batman.health, batman.demage)
