import random
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)
    left=[]
    right=[]
    mid=[]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            mid.append(i)
        else:
            right.append(i)
    return quicksort(left)+mid+quicksort(right)
arr=list(map(int,input("Enter The number : ").split(',')))
arr=quicksort(arr)
print(arr)