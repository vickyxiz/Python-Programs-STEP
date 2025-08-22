students = {}
while True:
    name = input("Enter student name: ")
    subjects = input("Enter favorite subjects (comma-separated): ")

    subject_list = [s.strip().lower() for s in subjects.split(",")]
    if name in students:
        students[name].update(subject_list)
    else: 
        students[name] = set(subject_list) 

    choice = input("Do you want to add another student? (yes/no): ").strip().lower()
    if choice != 'yes':
        break 
while True:
    update = input("\nDo you want to add more subjects to an existing student? (yes/no): ").strip().lower()
    if update != 'yes':
        break

    name = input("Enter the student name to update: ")
    if name in students:
        new_subjects = input("Enter new subjects (comma-separated): ")
        subject_list = [s.strip().lower() for s in new_subjects.split(",")]
        students[name].update(subject_list)
        print(f"Subjects updated for {name}.")
    else:
        print("Student not found.")
while True:
    search = input("\nDo you want to search for a student's subjects? (yes/no): ").strip().lower()
    if search != 'yes':
        break

    name = input("Enter student name to search: ")
    if name in students:
        print(f"{name}'s subjects: {', '.join(students[name])}")
    else:
        print("Student not found.")
while True:
    count = input("\nDo you want to count how many students like a subject? (yes/no): ").strip().lower()
    if count != 'yes':
        break

    subject = input("Enter the subject to search: ").strip().lower()
    total = 0
    for subs in students.values():
        if subject in subs:
            total += 1
    print(f"{total} student(s) like the subject '{subject}'.")

print("\n--- All Students and Their Subjects ---")
for name, subjects in students.items():

    print(f"{name}: {', '.join(subjects)}")


