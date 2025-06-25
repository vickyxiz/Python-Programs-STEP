n = input("Enter the elements: ")
arr = []
for i in n.split(','):
    arr.append(int(i))
order = input("Enter sorting order (ascending / descending): ").lower()

if order == "ascending":
    arr.sort()
    print("Sorted in Ascending Order:", arr)
elif order == "descending":
    arr.sort(reverse=True)
    print("Sorted in Descending Order:", arr)
else:
    print("Invalid input.")
