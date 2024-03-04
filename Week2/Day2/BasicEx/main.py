# Given this list:

# list1 = [5, 10, 15, 20, 25, 50, 20]

# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)

if index >= 0:
    list1[index] = 200
    print(f"Element is replaced: {list1}")
else:
    print(list1)


# Unpack the following tuple into 4 variables

# a_tuple = (10, 20, 30, 40)

a_tuple = (10, 20, 30, 40)

a, b, c, d = a_tuple

print(a)
print(b)
print(c)
print(d)

# Accept a number from the user and print its multiplication table
user_number = int(input("Give me a number: "))

numbers = list(range(1, 11))

for num in numbers:
    multiple = num * user_number
    print(multiple)


# Print the numbers from 1 to 10 using while loop
i = 0 
while i < 10:
    i += 1
    print(i)