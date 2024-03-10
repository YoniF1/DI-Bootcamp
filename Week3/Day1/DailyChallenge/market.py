# class Farm:

#     def __init__(self, name):
#         self.name = name
#         self.animals = {}

#     def add_animal(self, animal, number=1):
#         if animal in self.animals:
#             self.animals[animal] = self.animals[animal] + 1
#         else:
#             self.animals[animal] = number
    
#     def get_info(self):
#         output = f"{self.name}'s farm\n"
#         for k, v in self.animals.items():
#             output += f"{k} : {v}\n"
#         output += "E-I-E-I-0!"
#         return output
    
#     def get_animal_types(self):
#         types = list(self.animals.keys())
#         types.sort()
#         return types
        
#     def get_short_info(self):
#         pluralised = []
#         types = self.get_animal_types()
#         for animal in types:
#             if self.animals[animal] > 1:
#                 pluralised.append(animal + 's')
#             else:
#                 pluralised.append(animal)

#         output = f"{self.name}'s farm has"
#         for i, animal in enumerate(pluralised):
#             if i < len(pluralised) - 1:
#                 output += f" {animal},"
#             else:
#                 output += f" and {animal}."
#         return output

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
    
# print(macdonald.get_animal_types())
# print(macdonald.get_short_info())