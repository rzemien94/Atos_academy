from Hero import Hero

class SpiderMan(Hero):
    def __init__(self, name, demage, health, mana, money, spiders: int):
        super().__init__(name, demage, health, mana, money)
        self.spiders = spiders

    def attack_by_spiders(self,enemy):
        enemy.health -= (self.demage+1)
        self.spiders -= 1

    def increase_demage(self, i):
        self.demage += i