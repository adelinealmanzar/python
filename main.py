# exercise

# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
# newlist = [x for x in fruits if "a" in x]

nums = input('Numbers, please:').split(',')
squared_odd_nums = [int(num) ** 2 for num in nums if int(num) % 2 == 1]
print(squared_odd_nums)