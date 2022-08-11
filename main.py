# exercise

# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

x,y = map(int,input().split(','))
print(x)
lst = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(i*j)
    lst.append(row)

print(lst)
