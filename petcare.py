class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health 
    def show_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Health Level: {self.__health}")
    def care_action(self):
        print(f"{self.name} needs general care.")
    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Health must be between 0 and 100.")
class Dog(Pet):
    def care_action(self): 
        print(f"{self.name} needs a morning walk.")
class Rabbit(Pet):
    def care_action(self):
        print(f"{self.name} needs a calm place to rest.")
dog = Dog("mars", 68)
rabbit = Rabbit("astrox", 84)
pets = [dog,rabbit]
print("my pet care dashboard")
for pet in pets:
    pet.show_info()
    pet.care_action()
print()
print("updating pet health")
dog.set_health(90)
rabbit.set_health(90)
print("final pet care summary")
for pet in pets:
 pet.show_info()
 
