# exercise

# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

words = input('What is your input sentence?').split(' ')
words.sort()

freq = {}

for el in words:
    freq[el] = freq.get(el, 0) + 1


for key in freq:
    print(f'{key}:{freq[key]}')
    