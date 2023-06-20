# class naming convention: first letter of the word is uppercase
class Dog:
    # state/attributes
    def __init__(self,dog_name, dog_age, dog_breed, dog_weight):
        self.name = dog_name
        self.age = dog_age
        self.breed = dog_breed
        self.weight = dog_weight
    def __str__(self):
        return f"Dog: {self.name}, age: {self.age}"
    # methods/behaviours
    def eat(self): # self parameter during definition
        print("Nom nom")
        self.weight +=0.5
    
    def talk(self):
        print("Bark bark")

# create the object
# dog1 = Dog("Jett", 4 ,"pug", 12) # instantiate
# print(dog1)
# print(type(dog1))

# once created, by dot notation, can see all the things it has and can perform
# dog1.talk() # no self argument during calling of method

dog2 = Dog("Ninja", 13, "dutch-shepherd",23)
print(dog2.weight)
dog2.eat()
print(dog2.weight)