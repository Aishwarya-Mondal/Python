class Dog:
    def sound(self):
        print("dog barks")
class Cat:
    def sound(self):
        print("cat meows")
def makesound(animaltype):
    animaltype.sound()

catobj = Cat()
dogobj = Dog()
makesound(catobj)
makesound(dogobj)