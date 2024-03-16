from collections import Counter

class AnagramChecker:
    def __init__(self):
        with open('words.txt', 'r') as file:
            self.list_of_words = file.read().splitlines()
        self.list_of_anagrams = []

    def is_valid_word(self, word):
        if word.upper() in self.list_of_words:
            return True
        else:
            raise Exception("This word is not valid")
    
    def validate_word(self, word):
        word_list = word.split(' ')

        if len(word_list) != 1:
            raise Exception("Only one word is allowed")

        if not word_list[0].isalpha():
            raise Exception("Your word needs to be alphabetic")
        
        return True
        
    def get_anagrams(self, word):
        word_to_check = word.upper()
        word_counter = Counter(word_to_check)
        for other_word in self.list_of_words:
            if word_counter == Counter(other_word):
                self.list_of_anagrams.append(other_word)
       
        if word_to_check in self.list_of_words:
            self.list_of_anagrams.remove(word_to_check)

        sentence = ','.join(self.list_of_anagrams)
        print(f"YOUR WORD {word}\nthis is a valid English word\nAnagrams for your word {sentence}")
