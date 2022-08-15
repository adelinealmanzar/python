# exercise

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalizedwords = input().split(',')
lines = []

while True:
    s = input('What are your phases?')
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)