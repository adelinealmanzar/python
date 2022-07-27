from functools import reduce
# exercise

#square a list using a lambda expression
my_list = [5,4,3]
print(list(map(lambda el: el**2, my_list)))

# list sorting using a lambda expression
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda el: el[1])
print(a)