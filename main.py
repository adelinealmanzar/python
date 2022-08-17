# exercise

# Write a program that accepts a sentence and calculate the number of letters and digitsresult = []
text = input('Sentence please:')

uppercase = 0
lowercase = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
        

print(f'UPPER CASE {uppercase}\nLOWER CASE {lowercase}')
