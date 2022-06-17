import random

print(
    "This is a Rock-Paper-Scissors Game. \nWe will be using capital letters to represent each term while playing.\nR stands for Rock\nP stands for Paper \nS stands for Scissors")

# A Rock beats Scissors, Scissors beats Paper, and paper beats rock by covering it
game = ["R", "P", "S"]
computer_figure = random.choice(game)
#user_figure = ""

print("Play the game below by picking either Rock, Paper, or Scissors.")
user_figure = input("Ensure you type correctly. Pick between R, P, and S: ")
print("Computer choice is", computer_figure)

while user_figure not in ("exit", "Exit"):

    if user_figure == computer_figure:  # for a tie
        print("Player", (user_figure), " : Computer", (computer_figure))
        print("It is a Tie. \nPick again.")
        user_figure = input(
            "Ensure you type correctly. Pick between R, P, and S: ")
        continue

    elif user_figure == "R" and computer_figure == "P":
        print("Player", (user_figure), " : Computer", (computer_figure))
        print("Computer wins this round.")

    elif user_figure == "P" and computer_figure == "R":
        print("Player", (user_figure), " : Computer", (computer_figure))
        print("You win this round.")

    elif user_figure == "R" and computer_figure == "S":
        print("Player", (user_figure), " : Computer", (computer_figure))
        print("You win this round.")

    elif user_figure == "S" and computer_figure == "R":
        print("Player", (user_figure), " : Computer", (computer_figure))
        print("Computer wins this round.")

    elif user_figure == "S" and computer_figure == "P":
        print("Player", (user_figure), " : Computer", (computer_figure))
        print("You win this round.")

    elif user_figure == "P" and computer_figure == "S":
        print("Player", (user_figure), " : PComputer", (computer_figure))
        print("Computer wins this round.")

    else:
        print("Wrong move. Your input has to be as stated above. \nPick again.")
        user_figure = input(
            "Ensure you type correctly. Pick between R, P, and S: ")
        continue

    break
