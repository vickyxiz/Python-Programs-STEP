n=input("Enter Your Name : ")
subjects=int(input("Enter the Toatal Subjects : "))
marks=[]
for i in range(1,subjects+1):
    score=int(input(f"Enter the score in {i} : "))
    marks.append(score)
total=sum(marks)
average=(total)/subjects
print("Total : ",total)
print("Average : ",average)