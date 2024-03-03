import random

user_input = input("Please give a string: ")

length = len(user_input)

if length < 10:
    print("string is not long enough")
elif length > 10:
    print("string is too long")
else:
    print("perfect string")
    print("The first char is {} and last char is {}".format(user_input[0], user_input[-1]))

    final_string = ""
    for i in user_input:
        final_string += i
        print(final_string)

    ls = list(final_string)
    random.shuffle(ls)
    shuffled_string = ''.join(ls)

    print(shuffled_string)
