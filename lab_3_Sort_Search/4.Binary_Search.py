n = input("Enter the elements (comma-separated): ")
arr = []
for i in n.split(','):
    arr.append(int(i))
arr.sort() 
print("The Sorted Array:",arr)
target=int((input("Enter The target Element:")))
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return None
        
result=binary_search(arr,target)
if result!=None:
    print("The Element is Found at the index:",result)
else:
    print("Enter the correct target Element")