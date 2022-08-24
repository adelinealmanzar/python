# exercise

# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n
from tkinter import N


class Divisible():
    def by_7(self, n):
        for num in range(0, n + 1):
            if num % 7 == 0:
                yield num

for i in Divisible().by_7( int(input('Please enter a number:'))):
    print(i)
