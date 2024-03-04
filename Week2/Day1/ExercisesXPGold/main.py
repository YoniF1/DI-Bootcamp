# Exercise 1

print("Hello world\n" *4 + "I love python\n" * 4)

# Exercise 2

month = int(input("Choose a month from 1-12: "))

if month in range(3, 6):
    print("Spring")
elif month in range(6, 9):
    print("Summer")
elif month in range(9, 12):
    print("Autumn")
else:
    print("Winter")
