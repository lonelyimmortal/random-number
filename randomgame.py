import random

def run_game():
    secret_number = random.randint(1, 10)
    numberofchances = 0
    guess = 0
    while numberofchances < 3:
        # Enter correct form of number
        try:
            # get a number guess from the player
            user_input = input("Guess a number between 1 to 10 \n")
            guess = int(user_input)
        except ValueError:
            print("'{}' isn't a number! Please enter a number between 1 to 10.".format(user_input))
        else:
            # compare guess the secret number
            if guess == secret_number:
                print("You got it! My number was {} \n".format(secret_number))
                break            
            elif guess < secret_number:
                print("The number is higher than {}.".format(guess))
            elif guess > secret_number:
                print("The number is lower than {}.".format(guess))
            else:
                # print hit/miss
                print("That's not it!")

        numberofchances +=1
        
        if numberofchances < 3:
            # print hit/miss
            print("Don't worry! Try it again. It still remains {} chance(s).  \n".format(3 - numberofchances))           
        else:
            # print hit/miss
            print("Game Over. My number was {}. \n".format(secret_number))
        
    play_again = input("Do you want to play again? [Y/N]")
    if play_again.lower() != 'n':
        run_game()
    else:
        print("Hope to see you very soon!")

run_game()