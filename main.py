# exercise

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
text = input('What is your comma-separated sequence of numbers?')
text_list = text.split(',')
text_tuple = tuple(text_list)
print(text_list)
print(text_tuple)