students={}
while True:
    name=input("Enter The Student name : ")
    subjects=input("Enter Your Favourite ")
    subject_list=[s.lower() for s in subjects.split(',')]
    if name in students:
        students[name].update(subject_list)
    else:
        students[name]=set(subject_list)
    choice=input("Do you want to add another student(yes/no) : ").lower()
    if choice!='yes':
        break