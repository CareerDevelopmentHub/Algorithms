import random

user = int(input("scissors(0), rock(1), paper(2): "))
computer = random.randint(0,2)

if user == computer:
    print("The computer is paper. You are paper too. It is a draw")
elif user == 1:
    if computer == 0:
        print("The computer is scissor. You are rock. You won")
    else:
        print("The computer is paper. You are rock. You lose.")
elif user== 2:
    if computer == 1:
        print("The computer is rock. You are paper. You win!")
    else:
        print("The computer is scissor. You are paper. You lose.")
elif user == 0:
    if computer == 2:
        print("The computer is paper. You are scissors. You win!")
    else:
        print("The computer is rock. You are scissors. You lose.")
