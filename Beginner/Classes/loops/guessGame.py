from random import randint


correct_answer = randint(1, 100)
number_tries = 7
#choose difficulty

answer = int(input("guess: "))
i=1

#how many tries left before making another guess
while answer != correct_answer and i <number_tries:
    if answer < correct_answer:
        print("go higher")
        answer = int(input("Make another guess: "))
        i = i+1
    else:
        print("go lower")
        answer = int(input("Make another guess: "))
        i=i+1

if answer == correct_answer:
    print("Good job! the right answer is indeed "+ str(answer) + ". It took you " + str(i) + " tries.")
else:
    print("you have no tries left. Good luck next time.")


