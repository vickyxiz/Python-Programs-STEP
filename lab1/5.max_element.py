n=input("Enter Three Numbers : ")
arr=[]
for i in n.split(','):
    arr.append(int(i))
arr.sort(reverse=True)
print("The Largest Number : ",arr[0])
print("The Second Largest Number:",arr[1])