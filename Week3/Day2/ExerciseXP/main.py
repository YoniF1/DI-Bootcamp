#Exercise1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     pass


# all_cats = [Bengal("Golda", 27), Chartreux("Fred", 14), Siamese("Stuart", 4)]
# saras_pets = Pets(all_cats)
# saras_pets.walk()

#Exercise2

# class Dog():
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         print(f"{self.name} is barking")

#     def run_speed(self):
#         return(self.weight/self.age * 10)
    
#     def fight(self, other_dog):
#         if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
#             print(f"{self.name} has won the fight")
#         else:
#             print(f"{other_dog.name} has won the fight")

# dog1 = Dog("Golda", 100, 500)
# dog2 = Dog("Fred", 5, 40)
# dog3 = Dog("Stuart", 2, 45)

# dog2.fight(dog1)
# print(dog1.run_speed())
# dog1.bark()
# dog3.fight(dog2)
# dog3.bark()
# print(dog3.run_speed())

#Exercise3
# See petdog.py

#Exercise4

# class Family():
#     def __init__(self, last_name):
#         self.members = []
#         self.last_name = last_name

#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print("Congratulations on the birth")

#     def is_18(self, name):
#         for member in self.members:
#             if name in member:
#                 return True if member["age"] > 18 else False


#     def family_presentation(self):
#         print(self.last_name)

#         for member in self.members:
#             print(member)


# new_family = Family("Johnson")
# new_family.members =     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]

# new_family.born(name='John', age='0', gender='Male', is_child=True)
# new_family.is_18("John")
# new_family.family_presentation()


# #Exercise5
        
# class TheIncredibles(Family):
#     def __init__(self, last_name):
#         super().__init__(last_name)
#         self.members = []

#     def use_power(self):
#         for member in self.members:
#             if member['age'] > 18 or member['is_child'] == False:
#                 print(member['power'])
#             else:
#                 raise Exception('The member is not over 18 year olds')

#     def incredible_presentation(self):
#         print("Here is our powerful family")
#         super().family_presentation()

# incredible_family = TheIncredibles("Meir")
# incredible_family.members =    [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]

# incredible_family.incredible_presentation()
# incredible_family.born(name ='Jack',age = 0,gender='Male',is_child=True,power='Unknown Power',incredible_name='Baby Jack')
# incredible_family.incredible_presentation()
