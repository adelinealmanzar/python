# exercise

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of atext = input('Sentence please:')


input_num = input('Provide a number please:')

sum = 0
temp = input_num
for x in range(int(input_num)):
    sum += int(temp)
    temp += input_num

print(sum)
