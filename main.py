# exercise

# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumericallylines = []

words = input('Tell me your words:').split(' ')
words.sort()
print(set(words))
