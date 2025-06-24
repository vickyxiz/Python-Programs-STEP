n=int(input("Enter a Year : "))
if n%4!=0:
    print("Not a Leap Year")
elif n%100!=0:
    print("Leap Year")
elif n%400==0:
    print("Leap Year")
else:
    ("Not a Leap Year")