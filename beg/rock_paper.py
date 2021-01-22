from random import randint

def play():
    t = ["Rock", "Paper", "Scissors"]
#assign a random play to the computer
    computer = t[randint(0,2)]

    while True:
        player = input("Rock, Paper, Scissors? ").upper()
        if player == computer:
            print("Tie!")
            break
        elif player == "ROCK":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                break
            else:
                print("You win!", player, "smashes", computer)
                break
        elif player == "PAPER":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                break
            else:
                print("You win!", player, "covers", computer)
                break
        elif player == "SCISSORS":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                break
            else:
                print("You win!", player, "cut", computer)
                break
        else:
            print("That's not a valid play. Check your spelling!")
            break
        
def main():
    play()
    while 1:
        opt = str(input("Would you like to play again(Y/N): ").upper())
        if opt == "Y":
            play()
        else:
            break
if __name__ == "__main__":
    main()            