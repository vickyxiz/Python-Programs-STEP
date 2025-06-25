rows=int(input("Eneter The Number of rows : "))
col=int(input("Enter The Number of column : "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(col):
        val=input(f"Enter The value of[{i+1}][{j+1}] : ")
        if val=='':
            val=0
        else:
            val=int(val)
        row.append(val)
    matrix.append(row)
print("The 2D array is")
for row in matrix:
    for elem in row:
        print(elem,end=' ')
    print()
result=0
for row in matrix:
    result+=sum(row)
print("The Sum of 2D array is : ",result)