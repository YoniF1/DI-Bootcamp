#Exercise1

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat("Rover", 10)
# cat2 = Cat("Fred", 6)
# cat3 = Cat("Steve", 7)


# def find_oldest_cat(*cats):
# #     cats = {cat1.age: cat1.name, cat2.age: cat2.name, cat3.age: cat3.name}
# #     cat_ages = cats.keys()
# #     oldest = max(cat_ages)
# #     print(f"The oldest cat is {cats[oldest]} and is {oldest} years old")

#     oldest = max(cats, key=lambda cat: cat.age)

#     print(f"The oldest cat is {oldest.name} and is {oldest.age} years old")


# find_oldest_cat(cat1, cat2, cat3)


#Exercise2

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {(self.height * 2)}")


# davids_dog = Dog("Rex", 50)

# print(f"{davids_dog.name}")
# print(f"{davids_dog.height}cm")
# davids_dog.bark
# davids_dog.jump

# sarahs_dog = Dog("Teacup", 20)

# print(f"{sarahs_dog.name}")
# print(f"{sarahs_dog.height}cm")
# sarahs_dog.bark
# sarahs_dog.jump

## dogs = [sarahs_dog, davids_dog]
## tallest_dog = max(dogs, key= lambda dog : dog.height)
## print(f"{tallest_dog.name} is the tallest")

# if davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is the tallest")
# else:
#     print(f"{sarahs_dog.name} is the tallest")
    

#Exercise3
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for lyric in self.lyrics:
#             print(lyric)
        

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

# class Zoo:
#     def __init__(self, zoo_name):
#         self.zoo_name = zoo_name
#         self.animals = []
#         self.name = zoo_name

#     def add_animal(self, *new_animal):
#         if new_animal not in self.animals:
#             self.animals.extend(new_animal)
    
#     def get_animals(self):
#         for animal in self.animals:
#             print(animal)

#     def sell_animal(self, animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)   
        
#     def sort_animals(self):
#         self.animals.sort()

#         animal_dict = {}
#         number = 1
#         for animal in self.animals:
#             first_letter = animal[0]
#             if  not animal_dict:
#                 animal_dict[number] = animal
#             elif  first_letter == animal_dict[number][0][0]:
#                   animal_dict[number].append(animal)
#             else:
#                 number += 1
#                 animal_dict[number] = [animal]
    
#         return animal_dict

#     def get_groups(self):
#         sorted_animals = self.sort_animals()
#         for value in sorted_animals.values():
#             print(value)

            
# zooo = Zoo("Ramat Gan Safari")
# zooo.add_animal("Ape", "Bear", "Baboon", "Cat", "Cougar", "Eeel", "Emu", "Elephant")
# zooo.sell_animal("Elephant")
# zooo.sort_animals()
# zooo.get_groups()
# zooo.get_animals()

        
    