# from collections import Counter
# import string

# #pip install --user -U nltk
# import nltk
# # nltk.download('stopwords') uncomment for first time use
# from nltk.corpus import stopwords


# class Text:
#     def __init__(self, text):
#         self.text = text

#     def frequency_of_word(self, word):
#         list_text = self.text.split()
#         result = Counter(list_text)
#         try:
#             frequency = result[word]
#             print(f"The word {word} appears {frequency} times in the given text")
#         except:
#             print("Your word does not appear in the given text")
#             return None
            
        
#     def most_common_word(self):
#         list_text = self.text.split()
#         result = Counter(list_text)
#         most_common = result.most_common(1)
#         print(most_common[0][0])


#     def unique_words(self):
#         list_text = self.text.split()
#         unique = set(list_text)
#         unique_word_list = list(unique)
#         print(unique_word_list)
 
#     @classmethod
#     def from_file(cls, filename):
#         with open(filename, 'r') as file_obj:
#             text = file_obj.read()

#         return cls(text = text)

    
# # new_text = Text("Hello my name is Yoni and Hello this is a frequent word Hello does this work")

# # new_text.frequency_of_word('Hello')

# # new_text.most_common_word()
# # new_text.unique_words()

# # strangers_text = Text.from_file("the_stranger.txt")
# # strangers_text.most_common_word()
# # strangers_text.unique_words()


# class TextModification(Text):
#     def __init__(self, text):
#         super().__init__(text)

#     def remove_punctuation(self):
#         clean_text = self.text.translate(str.maketrans('', '', string.punctuation))
#         return clean_text
    
    
#     def remove_special_characters(self):
#         clean_text = ''
#         for letter in self.text:
#             if letter.isalnum():
#                 clean_text += letter
#         return clean_text
    
#     def remove_stop_words(self):
#         text = ' '.join([word for word in self.text.split() if word not in (stopwords.words('english'))]) 
#         return(text)


# strangers_text = Text.from_file("the_stranger.txt")

# modified = TextModification(strangers_text.text)

# strangers_text.frequency_of_word('Albert')
# strangers_text.most_common_word()
# strangers_text.unique_words()

# print(modified.remove_punctuation())
# print(modified.remove_special_characters())
# print(modified.remove_stop_words())
