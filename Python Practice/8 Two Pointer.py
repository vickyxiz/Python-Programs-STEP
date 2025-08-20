arr=list(map(int,input("Enter The Number : ").split(',')))
target=int(input("Enter The Target : "))
l=0
r=len(arr)-1
while l<r:
    if arr[l]+arr[r] == target:
        print(f"The Element is found by adding the index {l}, {r}")
        break
    elif arr[l]+arr[r] > target:
        r=r-1
    elif arr[l]+arr[r]< target:
        l=l+1
else:
    print("No Pair")

  
 

