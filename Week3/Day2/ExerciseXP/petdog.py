from main import Dog
import random

class PetDog(Dog):

    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        output=f"{self.name}, "
        for dog in args:
            output += f"{dog.name}, "
        
        print(f"{output}all play together")
        
    def do_a_trick(self):
        sentences = [f"{self.name} does a barrel roll", f"{self.name} stands on his back legs", f"{self.name} shakes your hand", f"{self.name} plays dead"]

        if self.trained == True:
            print(random.choice(sentences))

dog1 = PetDog("Freddy", 10, 10)
dog2 = Dog("Steve", 5, 20)
dog3 = Dog("Golda", 6, 8)
dog4 = PetDog("Benny", 2, 20)
dog1.train()
dog1.do_a_trick()
dog4.do_a_trick()
dog1.play(dog2, dog3)