import random
random_num = random.randint(1, 100)
attempts=0
while True:
    try:
        guess=int(input("Enter Your guess : "))
        attempts+=1
        if guess < 1 or guess>100:
            print("Guess a valid number : ")
            continue
        if guess==random_num:
            print(f"Yes The Correct number is {random_num}")
            print(f"The total attempt={attempts}")
            break
        elif guess<random_num:
            print("It's Too Low\n")
        else:
            print("it's Too High")
    except ValueError:
        print("Enter valid number")