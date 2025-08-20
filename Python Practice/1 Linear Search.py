arr=list(map(int,input("Enter The Elements : ").split(',')))
Target=int(input("Enter The Target Value : "))

i=0
while i< len(arr):
    if arr[i]==Target:
        print("The Element is found at index pos",i)
        break
    i+=1
else:
    print("The Element Is Not Found")