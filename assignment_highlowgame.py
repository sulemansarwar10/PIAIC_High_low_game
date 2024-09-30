#name suleman sarwar
#Roll#  PIAIC59391
##Python Programming Assignment 08 (B): High-Low Game

import random
round=1
score=0
while round<=5:
    print("Round",round)
    user_number=random.randint(1, 100)
    computer_number=random.randint(1, 100)
    round+=1
    print("Your number is",user_number)
    x=input("Do you think your number is higher or lower than the computer's?:")
    while (x!="lower" and x!="higher"):
        x=input("Do you think your number is higher or lower than the computer's?:")

    if user_number<computer_number and x=="lower":
        print("You were right! The computer's number was",computer_number)
        score+=1
    elif user_number>computer_number and x=="higher":
        print("You were right! The computer's number was",computer_number)
        score+=1
    else:    
        print("Aww, that's incorrect. The computer's number was",computer_number)
    print("Your score is now", score)   
    print("\n \n") 
print("Thanks for playing!")
print("Good job, you played really well!")
print("Your Score is",score)    