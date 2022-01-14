class Weapon:
    def __init__(self, attack, name):
        self.attack = attack
        self.name = name

class Character:
    def __init__(self, life, attack) -> None:
        self.life = life
        self.attack_point = attack

    def attack(self, target):
        target.get_hit(self.attack_point)

    def get_hit(self, damage):
        self.life -= damage

class Cratos(Character):
    def __init__(self, weapon: Weapon, name="Cratos") -> None:
        super().__init__(100, 10)
        self.experience = 0
        self.weapon = weapon
        self.name = name

    def gain_XP(self, amount):
        self.experience += amount
        bonus = self.experience//10
        self.attack_point += bonus
        self.experience -= bonus*10

    def set_weapon(self, weapon):
        self.weapon = weapon

    def hit(self, enemy):
        enemy.get_hit(self.weapon.attack)

    def __str__(self) -> str:
        return "{name} - {pv} points de vie - {xp} xp".format(name=self.name, pv=self.life, xp=self.experience)

class Drauf(Character):
    def __init__(self, life, attack_point=10):
        super().__init__(life, attack_point)


weapon = Weapon(15, "Anaconda")
player = Cratos(weapon, "Ta mère")
print(player)

enemy = Drauf(50, 10)