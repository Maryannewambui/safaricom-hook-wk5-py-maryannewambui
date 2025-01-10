class Superhero:
    def __init__(self, name, superpower, weakness):
        self.name = name
        self.superpower = superpower
        self.weakness = weakness

    def display_info(self):
        return f"Superhero: {self.name}, Superpower: {self.superpower}, Weakness: {self.weakness}"

    def fight_crime(self):
        return f"{self.name} is fighting crime with their {self.superpower}!"

class FlyingHero(Superhero):
    def __init__(self, name, superpower, weakness, flying_speed):
        super().__init__(name, superpower, weakness)
        self.flying_speed = flying_speed

    def display_info(self):
        return f"FlyingHero: {self.name}, Superpower: {self.superpower}, Weakness: {self.weakness}, Flying Speed: {self.flying_speed} mph"

    def fly(self):
        return f"{self.name} is flying at {self.flying_speed} mph!"

# instances
hero1 = Superhero("Green Lantern", "Power ring", "wood")
hero2 = FlyingHero("Super Man", "Super strength", "Kryptonite", 500)

# Displaying information
print(hero1.display_info())
print(hero2.display_info())

# Testing methods
print(hero1.fight_crime())
print(hero2.fly())
