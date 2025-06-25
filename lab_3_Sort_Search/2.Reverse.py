n=input("Enter The Elements:")
arr=[]
for i in n.split(','):
    arr.append(int(i))
#arr.reverse()
result= arr[::-1]
print(result)