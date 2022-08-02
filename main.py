# exercise

# Define a class which has at least two methods: 1. getString and 2.printString

class InputOutString():
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

ioString = InputOutString()
ioString.getString()
ioString.printString()