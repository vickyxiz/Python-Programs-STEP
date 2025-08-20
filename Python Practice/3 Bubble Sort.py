arr=list(map(int,input("Enter The Numbers : ").split(',')))
while True:
    A=True
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            A=False
    if A==True:
        break
print(arr)