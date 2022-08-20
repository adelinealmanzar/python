# exercise

# Write a program that computes the net amount of a bank account based a transaction log from console input.

input_log = input('Transaction Log:').split(" ")

balance = 0
for i, el in enumerate(input_log):
    if el == "D":
        balance += int(input_log[i + 1])
    elif el == "W":
        balance -= int(input_log[i + 1])

print(balance)
