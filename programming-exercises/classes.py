class Dog:
    name = ""
    age = 0
    fur = ""
    race = ""

    def __init__(self, name, age, fur, race):  # this method allows us to
        # pass arugments and change attributes of the instance when instanciating it
        self.name = name
        self.age = age
        self.fur = fur
        self.race = race

    def bark(self):
        print(f"{self.name} barks!")

    def show_attributes(self):
        attributes = {
            "name": self.name,
            "age": self.age,
            "fur": self.fur,
            "race": self.race
        }
        return attributes


tomas = Dog("Tomás", 6, "brown", "perro de agua")  # creating an instance of the class
print(tomas.show_attributes())


class Animal:
    species = ""
    length = ""
    width = ""
    weight = ""


class Dog(Animal):
    name = ""

    def __init__(self, name):  # this method allows us to
        # pass arugments and change attributes of the instance when instanciating it
        self.name = name

    def bark(self):
        print(f"{self.name} barks!")


pipo = Dog("pipo")
print(pipo.name)
pipo.species = "galgo"
print(pipo.species)
print(pipo.length)
print(isinstance(pipo, Dog))
print(isinstance(pipo, Animal))

