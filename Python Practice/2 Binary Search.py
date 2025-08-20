arr = list(map(int,input("Enter the elements : ").split(',')))
target = int(input("Enter the target : "))
l = 0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        print("Element is found at :",mid)
        break
    elif arr[mid]<target:
        l=mid+1
    else:
        r=mid-1
else:
    print("Element is not found")

    
