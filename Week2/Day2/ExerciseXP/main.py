# # Exercise1
# my_fav_numbers = {1, 2, 3, 4}
# my_fav_numbers.add(5)
# my_fav_numbers.add(6)

# number_list = list(my_fav_numbers)
# number_list.pop()
# my_fav_numbers = set(number_list)

# friends_fav_numbers = {12, 13, 15, 17}

# our_fav_numbers = my_fav_numbers.union(friends_fav_numbers)
# print(our_fav_numbers)


# # Exercise2

# # No a tuple is immutable

# # Exercise3

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# len(basket)
# basket.clear()
# print(basket)

#Exercise4
# A float is a number with a decimal, integer doesn't have decimal point


# Mix of integers & floats 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5

# integer_list = list()
# float_list = list()

# count = 0
# integer = 2
# flt = 1.5

# while count < 4:
#     count += 1
#     integer_list.append(integer)
#     float_list.append(flt)

#     integer += 1
#     flt += 1.0

# final_list = float_list + integer_list
# final_list.sort()
# print(final_list)

# random.random() and append float value to list

# Exercise5

# for i in range(1, 21):
#     print(i)

# for i in range(1, 21):
#     print(i) if i % 2 == 0 else False

# Exercise6

# while True:
#    user_input = input("State your name: ")
#    if user_input == "Yoni":
#        break
#    else:
#        continue
   

# Exercise7
   
# user_input = input("What is your favourite fruit? Separate fruits with a space ")
# favourite_fruit_list = user_input.split()
# fruit = input("Enter the name of a fruit ")

# if fruit in favourite_fruit_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

#Exercise8
# topping_list = []
# sum = 0

# while True:
#     user_input = input("Give a pizza topping: ")
#     if user_input == "quit":
#         break
#     else:
#         topping_list.append(user_input)
#         print("I'll add that to the pizza")

#     sum = len(topping_list) * 2.5 + 10

# print(f"{','.join(topping_list)} are the toppings of your pizza and it costs £{sum} in total")


# Exercise9

# num = 0
# total_number_in_family = 0
# total_number_in_family = int(input("How many people in your family?: "))
# ticket_price = 0

# while num < total_number_in_family:
#     num+=1
#     age = int(input(f"How old is your family member? "))

#     if age < 3:
#         continue
#     elif age >= 3 and age <= 12:
#         ticket_price += 10
#     else:
#         ticket_price += 15

# print(f"The total price is ${ticket_price}")

# Exercise9 Part 4
# name_list = ["Benny Gantz", "Abba Eban", "Golda Meir", "David Ben Gurion"]
# copy_of_list = name_list.copy()

# for nm in copy_of_list:
#     age = int(input(f"How old is {nm}? "))

#     if age not in range(16, 22):
#         name_list.remove(nm)
#     else:
#         continue

# print(name_list)

#Exercise 10

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
copy_of_sandwich = sandwich_orders.copy()
finished_sandwiches = []

i=0
while i < len(copy_of_sandwich) - 1:
    i+=1

    if copy_of_sandwich[i] == "Pastrami sandwich":
        sandwich_orders.remove(copy_of_sandwich[i])
    else:
        continue

copy_of_sandwich2 = sandwich_orders.copy()
for j in copy_of_sandwich2:
    sandwich = sandwich_orders.pop(sandwich_orders.index(j))
    finished_sandwiches.append(sandwich)

for x in finished_sandwiches:
    print(f"I made your {x}")

