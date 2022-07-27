from functools import reduce
# exercise

#square a list using a lambda expression
my_list = [5,4,3]
print(list(map(lambda el: el**2, my_list)))