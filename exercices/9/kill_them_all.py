class Character:
    def __init__(self, life, attack) -> None:
        self.life = life
        self.attack_point = attack

    def attack(self, target):
        target.get_hit(self.attack_point)

    def get_hit(self, damage):
        self.life -= damage


class Cratos(Character):
    def __init__(self) -> None:
        super().__init__(100, 10)
        self.experience = 0

    def gain_XP(self, amount):
        self.experience += amount
        bonus = self.experience//10
        self.attack_point += bonus
        self.experience -= bonus*10


class Drauf(Character):
    def __init__(self, life, attack_point):
        super().__init__(life, attack_point)
