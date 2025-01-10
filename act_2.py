class Animal:
    def move(self):
        pass

class Cat(Animal):
    def move(self):
        return "play a lot"

class Bird(Animal):
    def move(self):
        return "Flying in the sky"

# instances
cat = Cat()
bird = Bird()

# polymorphism
animals = [cat, bird]
for animal in animals:
    print(animal.move())
