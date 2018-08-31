class Cat():
    species = "russian blue"

    def __init__(self, name):
        self.name = name

cat1 = Cat("냥1")
cat2 = Cat("냥2")

print(cat1.species)
print(cat2.species)

print(cat1.name)
print(cat2.name)