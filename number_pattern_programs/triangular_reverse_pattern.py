num = int(input("Enter a number : "))

# Here i in the loop acts as the row
# and j in the loop acts as the column of numbers
for i in range(num, 0, -1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()