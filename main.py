# exercise

class User():
    def __init__(self, name):
        self.name = name

class Wizard(User):
    def __init__(self, name):
        super().__init__(name)

wizard = Wizard('me')
print(wizard.name)