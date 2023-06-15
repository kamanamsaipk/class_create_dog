# Assignment-2
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def bark(self):
        print("Woof! Woof!")
    def favourite_food(self):
        print(" chicken leg piece")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def snore(self):
        print(" fzfzzzzfzzzfzzzz...")
    def height(self):
        print("medium ")

dog1 = JackRussellTerrier("Jack", 3, "Brown")
dog2 = Bulldog("Buddy", 5, "Black")

dog1.description()
dog1.bark()
dog1.favourite_food()
dog1.get_info()

dog2.description()
dog2.snore()
dog2.height()
dog2.get_info()