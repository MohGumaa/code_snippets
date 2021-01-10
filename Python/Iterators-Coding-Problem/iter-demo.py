
# class Sentence:

#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration
#         index = self.index
#         self.index += 1
#         return self.words[index]


# def sentence(sentence):
#     for word in sentence.split():
#         yield word

# def sentence(sentence):
#     words = sentence.split()
#     index = 0
#     while index < len(words):
#         yield words[index]
#         index += 1

my_sentence = sentence('This is a test')

# By default spilt in space delimater
# print('This is a test'.split())

for word in my_sentence:
    print(word)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))


# This should have the following output:
# This
# is
# a
# test
