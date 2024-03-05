#Exercise1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dict = dict(zip(keys, values))
# print(dict)


#Exercise2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# total_cost = 0
# individual_cost = 0

# for name, age in family.items():
#     if age < 3:
#         continue
#     elif age >= 3 and age <= 12:
#         total_cost += 10
#         individual_cost += 10
#     else:
#         total_cost += 12
#         individual_cost += 12
#     print(f"{name} pays {individual_cost}")
#     individual_cost = 0


# print(f"The family's total cost is {total_cost}")

#Exercise2BONUS

# family = {}

# total_cost = 0
# individual_cost = 0

# number_of_people = int(input("How many people in your family?"))

# i=0
# while i < number_of_people:
#     name_of_person = input("What is your name: ")
#     age_of_person = int(input("What is your age: "))
#     family[name_of_person] = age_of_person
#     i+=1

# for name, age in family.items():
#     if age < 3:
#         individual_cost = 0
#     elif age >= 3 and age <= 12:
#         total_cost += 10
#         individual_cost += 10
#     else:
#         total_cost += 12
#         individual_cost += 12
#     print(f"{name} pays ${individual_cost}")
#     individual_cost = 0

# print(f"The family's total cost is ${total_cost}")

#Exercise3

# brand = { 
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": ["Amancio", "Ortega", "Gaona"],
#     "type_of_clothes":["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": 
#         { 
#            "France": "blue", 
#             "Spain": "red", 
#             "US": ("pink", "green")
#         }
# }

#3

# brand["number_stores"] = 2

#4

# print(brand["type_of_clothes"][:3])


#5
# brand["country_creation"] = "Spain"

#6
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")

# print(f"{brand["international_competitors"]}")


#7
# del brand["creation_date"]

#8

# print(f"{brand["international_competitors"][-1]}")

#9
# print(f"{brand["major_color"]["US"]}")

#10

# print(len(brand))

#11

# for key in brand.keys():
#     print(key)

#12

# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }

#13
# brand.update(more_on_zara)
# print(brand)

#14
# print(brand["number_stores"])
#The update method overwrote the previous value as the keys matched

#Exercise4

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_A = {}

# for i, user in enumerate(users):
#     disney_users_A[user] = i

# print(disney_users_A)

# disney_users_B = {}

# for i, user in enumerate(users):
#     disney_users_B[i] = user

# print(disney_users_B)

# disney_users_C = {}

# users.sort()

# for i, user in enumerate(users):
#     disney_users_C[user] = i

# print(disney_users_C)


# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_D = {}

# for i, user in enumerate(users):
#     if "i" in user:
#         disney_users_D[user] = i
#     else:
#         continue

# print(disney_users_D)


# disney_users_E = {}

# for i, user in enumerate(users):
#     if user.startswith("M") or user.startswith("P"):
#         disney_users_E[user] = i
#     else:
#         continue

# print(disney_users_E)




