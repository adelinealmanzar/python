# exercise

# Write a program that accepts a sentence and calculate the number of letters and digitsresult = []
text = input('Letters and Digiits plaase:')

letters = 0
digits = 0
for char in text:
    if ('a' <= char and char <= 'z') or ('A' <= char and char <= 'Z'):
        # if it's a digit
        letters += 1
    elif '0' <= char and char <='9':
        #if it's a letter
        digits += 1


print(f'DIGITS {digits}\nLETTERS {letters}')  
