user_input = input("Please give a string: ")

length = len(user_input)

if length < 10:
    print("string is not long enough")
elif length > 10:
    print("string is too long")
else:
    print("perfect string")

# OR

# count = 0

# for i in user_input:
#     count += 1

# if count < 10:
#     print("string is not long enough")
# elif count > 10:
#     print("string is too long")
# else:
#     print("perfect string")


print(user_input[0])
print(user_input[-1])

final_string = ""
for i in user_input:
    final_string += i
    print(final_string)

p