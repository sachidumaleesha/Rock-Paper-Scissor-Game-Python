import random

choices = ["rock","paper","scissor"]

computer = random.choice(choices)
player = None

print("Rock | Paper | Scissor")

while True:
    while player not in choices:
        player = input("Enter your choice: ").lower()

    print("Computer: ", computer)
    print("Player: ", player)

    if player == computer:
        print("Match draw :|")
    elif player == 'rock':
        if computer == 'paper':
            print('Computer win :(')
        elif computer == 'scissor':
            print("You Win :)")
    elif player == 'paper':
        if computer == 'rock':
            print("You win :)")
        elif computer == 'scissor':
            print("computer win :(")
    elif player == 'scissor':
        if computer == 'paper':
            print('You win :)')
        elif computer == 'rock':
            print('Computer win :(')

    play_again = input("Do you want to play again? (yes/no): ").lower()
    player = None

    if play_again != 'yes':
        break
print('Bye!')
