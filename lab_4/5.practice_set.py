my_set={'ram','sam','tom'}
print("This is The default Names : ",my_set)
b=input("Enter The Name to update in the set : ")
my_set.add(b)
print("Updated Names: ",my_set)
remove=input("Enter the name to remove : ")
my_set.remove(remove)
print(my_set)
check=input("Check the name is present or not :").lower()
lower_set = {name.lower() for name in my_set}
if check in my_set:
    print("The Name is found")
else:
    print("The element is not  found")