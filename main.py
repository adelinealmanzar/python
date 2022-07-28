# exercise

#error handling
while True:
    try:
        age = int(input('what is your age'))
        raise ValueError('look at me!')
    except ZeroDivisionError as err:
        print(err)
    else: #else if we don't run into an error and the user enters valid information
        print('thank you!')
        break