rows = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(col):
        val = input(f"Enter the value of [{i+1}][{j+1}]: ")
        if val == '':
            val = 0
        else:
            val = int(val)
        row.append(val)
    matrix.append(row)
print("\nThe 2D array is:")
for row in matrix:
    print(row)
target = int(input("\nEnter the Target value: "))
found = False
for i in range(rows):
    for j in range(col):
        if matrix[i][j] == target:
            print(f"Target found at position [{i+1}][{j+1}]")
            found = True

if not found:
    print("The target element is not found.")
