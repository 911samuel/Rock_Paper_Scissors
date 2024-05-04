import random

user_wins = 0
computer_wins = 0
tie = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue

    random_pick = random.randint(0,2)
    computer_pick = options[random_pick]
    print("Computer picked", computer_pick)

    if user_pick == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1
    elif user_pick == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
    elif user_pick == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
    elif user_pick == "rock" and computer_pick == "rock":
        print("Tie")
        tie += 1
    elif user_pick == "paper" and computer_pick == "paper":
        print("Tie")
        tie += 1
    elif user_pick == "scissors" and computer_pick == "scissors":
        print("Tie")
        tie += 1
    else:
        print("you lost!")
        computer_wins += 1
print("You win", user_wins, "times.")
print("Computer win", computer_wins, "times.")
print("Tie", tie, "times.")
print("Goodbye!")

