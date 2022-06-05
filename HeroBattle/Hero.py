class Hero:
    def __init__(self, name: str, demage: int, health: int, mana: int, money: int):
        self.name = name
        self.demage = demage
        self.health = health
        self.mana = mana
        self.money = money

    def rest(self):
        self.mana += 20

    def attack(self, enemy):
        enemy.health -= self.demage

    def rob(self,enemy):
        self.money += enemy.money
        enemy.money = 0
