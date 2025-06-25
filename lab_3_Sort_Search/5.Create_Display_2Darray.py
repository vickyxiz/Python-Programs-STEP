rows=int(input("Enter The Number of Rows: "))
col=int(input("Enter The Number of Col: "))
matrix=[]
print("Enter The Elements Row Wise \"FOR 0 JUST ENTER\"")
for i in range(rows):
    row=[]
    for j in range(col):
        val=input(f"Enter The Values[{i+1}][{j+1}]: ")
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
    print( )