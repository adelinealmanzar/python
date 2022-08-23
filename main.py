# exercise

# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. 
lst = []

while True:
    s = input('Names, Ages, and Scores:').split(',')
    if not s[0]:
        break
    lst.append(tuple(s))

print(lst.sort(key= lambda x: (x[0], int(x[1]), int(x[2]))))
