question1 = "what is France capital ? "
question2 = "what is (5+3*3)^2  ? "
question3 = "what is the largest animal on earth?"



print("Welcome to the quiz game")

print("Question1: " + question1)
answer1 = input("answer: ")

if answer1 == "Paris" or answer1 == 'paris':
    print("good job! there are 2 questions remaining.")
    
    print("Question2: " + question2)
    answer2 = input("answer: ")
    if answer2 == "196":
        print("good job! there is only 1question remaining.")
    
        print("Question3: " + question3)
        answer3 = input("answer: ")
        if answer3 == "whale" or answer2=="Whale":
            print("Good job! you got it all right")
        else:
            print("Hard luck! you failed at your last question! you will get it next time")
    else:
        print("you got the second question wrong! good luck next time!")

else:
    print("You got the first answer wrong. try again.")



