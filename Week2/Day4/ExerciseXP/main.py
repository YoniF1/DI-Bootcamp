import random

#Exercise1

# def display_message():
#     print("I am learning how to create functions in Python")

# display_message()

#Exercise2

# def favourite_book(title):
#     print(f"One of my favourite books is {title}")

# favourite_book("Harry Potter")

#Exercise3

# def describe_city(city, country = "Israel"):
#     print(f"{city} is in {country}")


# describe_city("London", "United Kingdom")

#Exercise4
# import random

# def compare_number(number):
#     random_number = random.randint(1, 100)

#     if number == random_number:
#         print("Success the numbers are the same")
#     else:
#         print(f"The numbers are different {number} and {random_number}")

# compare_number(50)
# compare_number(42)

#Exercise5

# def make_shirt(size = "large", text = "I love python"):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt()
# make_shirt("medium")
# make_shirt("small", "keep calm and carry on")
# make_shirt(size = "large", text = "i love python")


#Exercise6

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magician_names):
#     for magician in magician_names:
#         print(magician)

# show_magicians(magician_names)

# def make_great(magician_names):
#     for i in range(len(magician_names)):
#         magician_names[i] += ' is Great'
    
#     return magician_names

# make_great(magician_names)
# show_magicians(magician_names)

#Exercise7
# def convert_month_to_season(month):
#     month_to_season= {
#         "winter": [1,2,12],
#         "summer": [6,7,8],
#         "autumn": [9,10,11],
#         "spring": [3,4,5]
#     }

#     season=''
#     for k, v in month_to_season.items():
#         if month in v:
#             season = k
#     return season

# def get_random_temp(month):
#     season = convert_month_to_season(month)

#     if season == 'winter':
#         temperature = random.randint(-10, 10)
#     elif season == 'spring':
#         temperature = random.randint(10, 20)
#     elif season == 'autumn':
#         temperature = random.randint(0, 20)
#     else:
#         temperature = random.randint(20, 40)

#     return temperature

# def main():
#     month = int(input("Type in a month: "))
#     temp = get_random_temp(month)

#     if temp < 0:
#         message = ("it's freezing!")
#     elif temp in range(0, 17):
#         message = ("quite chilly!")
#     elif temp in range(16, 23):
#         message = ("nice, lucky")
#     elif temp in range(24, 33):
#         message = ("warm isn't it")
#     else:
#         message = "Turn on the air conditioner"
    
#     print(f"The temperature right now is {float(temp)} - {message}")

# main()
    
#Exercise8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_questions_receive_answer():
    wrong_answers = []
    wrong_questions = []
    correct_answers = []

    correct_score = 0
    incorrect_score = 0
    
    for i, quiz in enumerate(data):
        answer = input(f"{data[i]["question"]}\n")

        if answer == data[i]["answer"]:
            correct_score += 1
        else:
            incorrect_score += 1
            wrong_answers.append(answer)
            wrong_questions.append(data[i]["question"])
            correct_answers.append(data[i]["answer"])

    print(f"The number of your correct answers is {correct_score} and incorrect is {incorrect_score}")
    
    wrong_dict = dict(zip(wrong_questions, zip(wrong_answers, correct_answers)))

    for question, answer in wrong_dict.items():
        print(f"Your answer '{answer[0]}' was incorrect to the question '{question}', the correct answer is '{answer[1]}'\n")
    
    if incorrect_score > 3: print("Since you had more than 3 incorrect answers, you will need to play again")

ask_questions_receive_answer()