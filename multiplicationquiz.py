#Nick Hu
#1/9/25

#Init
import random
right = 0
wrong = 0
#Functions
def multiquiz():
    global right
    global wrong
    print("Prepare for this multiplication quiz..")
    for i in range(5): #Amount of questions
        print(f"Question {i + 1} of 5") #Questions given code (Adds 1 per question)
        result1 = int(random.randint(1,10)) #Computer generates random number to multiply
        result2 = int(random.randint(1,10)) #Computer generates random number to multiply
        print("What is " + str(result1) +"*"+ str(result2))
        answer1 = result1 * result2
        player1ans = int(input("Your answer"))
        if player1ans == answer1:
            print("You got #1 right. The answer was " + str(answer1))
            right = right + 1
        else:
            print("You got #1 wrong. The answer was " + str(answer1))
            wrong = wrong + 1

        print("You got " + str(right) + " answers right.")
        print("You got " + str(wrong) + " answers wrong.")

multiquiz()
