n = int(input("Enter the number of elements (size of the array): "))
arr = []

for i in range(n):
    val = input(f"Enter element {i+1}: ")
    arr.append(val)

print("The array is:", arr)
