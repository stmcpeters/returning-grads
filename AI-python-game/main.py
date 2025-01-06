# imports the random module to generate a random choice for the computer
import random

# function to get the computer's choice
# random.choice() picks a random element from a list
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# main function to run the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # get the user's choice
        # strip() removes any leading/trailing whitespace
        # lower() converts the input to lowercase
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").strip().lower()

        # break statement to exit the game if user types 'quit'
        if user_choice == 'quit':
            print("Thanks for playing!")
            break

        # checks if the user entered a valid choice (either rock, paper, or scissors)
        # prints error message and restarts the loop if not valid
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
        
        # get the computer's choice
        computer_choice = get_computer_choice()
        
        # display the choices
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        # choose the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
# main execution block
if __name__ == "__main__":
    main()
