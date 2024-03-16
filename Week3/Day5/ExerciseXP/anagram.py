from anagram_checker import AnagramChecker
#Run from ExerciseXP folder

def ask_for_word():
    user_input = ''
    while user_input != 'exit':
        user_input = input("Choose a word to check for anagrams in the text: ")
        anagram_checker = AnagramChecker()
        anagram_checker.validate_word(user_input)
        anagram_checker.is_valid_word(user_input)
        anagram_checker.get_anagrams(user_input)
        
ask_for_word()