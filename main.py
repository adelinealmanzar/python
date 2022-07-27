from functools import reduce
# exercise

#return duplicates in list using a comprehension
some_list = ['a','b','c','b','d','m','n','n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)


comp_duplicates = list(set([el for el in some_list if some_list.count(el) > 1]))
print(comp_duplicates)