from Hero import Hero

class Batman(Hero):
    def __init__(self, name, demage, health, mana, money, car: str):
        super().__init__(name, demage, health, mana, money)
        self.car = car

    def increase_demage(self, i):
        self.demage += i

    def buy_new_car(self,car,cost):
        self.car = car
        self.money -=cost