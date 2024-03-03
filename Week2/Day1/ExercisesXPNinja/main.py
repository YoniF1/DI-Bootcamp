# 3 <= 3 < 9 is True
# 3 == 3 == 3 is True
bool(0) is False
bool(5 == "5") is False
bool(4 == 4) == bool("4" == "4") is True
bool(bool(None)) is True


x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

# print("x is", x) is True
# print("y is", y) is False
# print("a:", a) is 5
# print("b:", b) is 10

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
           Ut enim ad minim veniam, quis nostrud exercitation ullamco
           laboris nisi ut aliquip ex ea commodo consequat.
           Duis aute irure dolor in reprehenderit in voluptate velit
           esse cillum dolore eu fugiat nulla pariatur.
           Excepteur sint occaecat cupidatat non proident,
           sunt in culpa qui officia deserunt mollit anim id est laborum."""

# with whitespace
print(len(my_text))  

# without whitespace
print(len(my_text) - my_text.count(' '))

previous = ""

while True:
    user_input = input("Enter the longest word without character 'A': ")
    if "a" in user_input.lower():
        print("Try again without an 'A' character")
        break
    elif len(user_input) > len(previous):
        print(f"Congratulations your new high score is {len(user_input)}")
        previous = user_input
    else:
        print(f"Your high score remains {len(previous)}, try one more time")
     