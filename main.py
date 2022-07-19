# exercise

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Orange', 10)
cat2 = Cat('Oreo', 5)
cat3 = Cat('Garfield', 9)


# 2 Create a function that finds the oldest cat
def oldest_cat(*cat_ages):
    return max(cat_ages)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_age = oldest_cat(cat1.age,cat2.age,cat3.age)
print(f"The oldest cat is {oldest_age} years old.")