# Exercise 1

print("Hello world\n" * 5)

# Exercise 2
print((99**3)*8)

# Exercise 3

# 5 < 3 is False
# 3 == 3 is True
# 3 == "3" is False
# '3' > 3 is error
# "Hello" == 'hello' is False

# Exercise 4

computer_brand = 'Apple'
print(f"I have an {computer_brand} computer")

# Exercise 5
name = "Yoni"
age = 30
shoe_size = 9
info = "My name is {}, I am {} years old, my shoe size is {}".format(name, age, shoe_size)
print(info)

# Exercise 6 
a = 9
b = 10
if a > b:
    print("Hello World")
else:
    print("Goodbye World")

# Exercise 7
    
number = int(input("Please give a number: "))
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

# Exercise 8
    
name = input("State your name: ")
if name == "Yoni":
    print("Great choice of name")
else:
    print("You have a bad name")

# Exercise 9

height = input("Give your height in inches: ")
height_in_cm = int(height) * 2.54

if height_in_cm > 145:
    print("You are tall enough to ride the ride")
else:
    print("Eat more veggies")