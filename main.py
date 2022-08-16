# exercise

# Write a program that accepts a sentence and calculate the number of letters and digitsresult = []
text = input('Letters and Digiits plaase:')

letters = 0
digits = 0
for char in text:
    print(digits, letters)
    if char.isdigit():
        print('here')
        # if it's a digit
        digits += 1
    elif char.isalpha():
        #if it's a letter
        letters += 1

print(f'DIGITS {digits}\nLETTERS {letters}')  
