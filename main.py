# exercise

#error handling
while True:
    try:
        age = int(input('what is your age'))
        10/age
        print(age)
    except (ValueError, ZeroDivisionError) as err:
        print(err)
    else: #else if we don't run into an error and the user enters valid information
        print('thank you!')
        break