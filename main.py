# exercise

#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
def div_by_7_not_5(num1, num2):
    result = []
    for i in range(num1, num2 + 1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(str(i))
    return ','.join(result)

print(div_by_7_not_5(2000,3200))