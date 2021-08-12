class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def show(self):
        print(f"I am {self.name}")

    def speak(self):
        print(f"Hello")


class Cat(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour

    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


if __name__ == "__main__":
    pet = Pet("John", 20)
    pet.speak()

    cat = Cat("Mary", 12, "Brown")
    cat.speak()

    dog = Dog("Alex", 6)
    dog.speak()



