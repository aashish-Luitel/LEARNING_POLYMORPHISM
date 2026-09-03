class animal:
    def speak(self):
        print("animal makes a speak")

class dog(animal):
    def speak(self):
        print("woof!")

class cat(animal):
    def speak(self):
        print("meow")

class cow(animal):
    def speak(self):
        print("moooo!!!")

Dog = dog()
Cat = cat()
Cow = cow()

Dog.speak()
Cat.speak()
Cow.speak()