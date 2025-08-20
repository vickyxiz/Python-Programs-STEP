arr=[5,4,2,6,1]
for i in range(0,len(arr)-1):
    min=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print(arr)