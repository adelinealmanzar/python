# exercise

# Define a class, which have a class parameter and have a same instance parameter.
class Animal():
    animal_type = 'Animal'

    def __init__(self, animal_type = None):
        self.animal_type = animal_type

a = Animal('Dog')
print(a.animal_type) #=> 'Dog'
print(Animal.animal_type) #=> 'Animal'
print(Animal().animal_type) #=> None