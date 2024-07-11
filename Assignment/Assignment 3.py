import random
while True:
 print("\nWelcome to Guessing Game!\n")
 low=1
 high=50
 val=random.randint(low,high)

 print("(Hidden number is {})\n\n".format(val))
 flag=True
 for i in range(0,5):
    print("Chances left:{}".format(5-i))
    guess=int(input("Guess the number: "))

    if guess==val:
        print("\nYou Win!!!!\n")
        flag=False
        break

    elif guess<val:
        print("Correct Answer is greater!\n")

    elif guess>val:
        print("Correct answer is smaller!\n")

 if flag:
   print("You Lose!!!!\n")

 print("Press 1 to Play again or 0 to quit")
 check=int(input("Enter your choice: "))
 if check==1:
     continue
 elif check==0:
     break

print("\nThanks for playing!\n")