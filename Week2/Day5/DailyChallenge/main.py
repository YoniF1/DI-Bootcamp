#Challenge1
# string = "without,hello,bag,world"
# list = [word for word in string.split(',')]
# list.sort()
# print(','.join(list))

#Challenge2

# def longest_word(sentence):
#     sentence_list = sentence.split(' ')
#     stack = []
#     for word in sentence_list:
#         if not stack:
#             stack.append(word)
#         elif len(word) > len(stack[0]):
#             stack.pop()
#             stack.append(word)

#     print(stack[0])
        
# test_sentences = ["Margaret's toy is a pretty doll.", "A thing of beauty is a joy forever.", "Forgetfulness is by all means powerless!" ]

# for sentence in test_sentences:
#     longest_word(sentence)
