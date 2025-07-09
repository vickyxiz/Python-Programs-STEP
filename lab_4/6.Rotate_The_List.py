def rotate(arr,k):
    k = k % len(arr)
    result = arr[-k:] + arr[:-k]
    print("Rotated List:", result)
arr = eval(input("Enter the list : "))
k = int(input("Enter the number of rotations: "))
rotate(arr,k)
