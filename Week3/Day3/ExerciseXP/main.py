# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         if self.amount > 1:
#             return f"{self.amount} {self.currency}s"
#         else:
#             return (self.amount, self.currency)
        
#     def __int__(self):
#         return self.amount
            
#     def __repr__(self):
#         if self.amount > 1:
#             return f"{self.amount} {self.currency}s"
#         else:
#             return (self.amount, self.currency)
        
#     def __add__(self, other):
#         if type(other) == int:
#             return self.amount + other
#         elif type(other) == Currency and self.currency == other.currency:
#             return self.amount + other.amount
#         elif self.currency is not other.currency:
#             raise Exception(f"{TypeError} cannot add between Currency type {self.currency} and {other.currency}")
#         else:
#             return
        
#     def __iadd__(self, other):
#         if type(other) == int:
#             self.amount += other
#             return self
#         elif type(other) == Currency:
#             self.amount += other.amount
#             return self
#         else:
#             return

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)

# print(c1) 
# # __str__
# # You don't need to do str(c1)

# print(int(c1))

# print(repr(c1))
# print(c1 + 5)
# print(c1 + c2)

# print(c1)

# c1 += 5
# print(c1)
# c1 += c2\
# # It works because we overloaded __str__ before
# print(c1)
# print(c1 + c3)

#Exercise2
#see func.py & exercise_one.py

#Exercise3

# import string
# import random


# random_string = ''.join(random.choices(string.ascii_letters, k=5))
# print(random_string)

#Exercise4

# from datetime import date, datetime

# today = date.today()
# print(today)

# #Exercise5

# today = datetime.now()
# jan = datetime(2025, 1,1)
# diff = jan - today

# print(diff)

#Exercise6

# birthday = datetime.datetime(1993, 2, 2)
# today = datetime.datetime.now()

# how_long = today - birthday
# print(f"They have lived for {how_long}")


#Exercise7
# from faker import Faker
# fake = Faker()

# def add_dictionary(number_of_dicts, fake):
#     number = 0
#     users = []
#     while number < number_of_dicts:
#         users.append({
#             'name': fake.name(),
#             'address': fake.address(),
#             'language_code': fake.language_code()
#         })
#         number+=1

#     print(users)

# add_dictionary(5, fake)
