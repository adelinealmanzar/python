# exercise

def highest_even(li):
    max = 0
    for num in li:
        if num % 2 == 0 and num > max:
            max = num
    return max

print(highest_even([10,2,3,4,5,8,11]))
