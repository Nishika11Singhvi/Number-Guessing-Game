number = 9
chances = 0
while (chances < 5):
    guess = int(input("Guess a number between 1 to 9: "))
    if (guess > number):
        print("Your guess is too big. Enter a number that is not", guess)
    elif (guess == number):
        print("Congratulations! Your guess is correct")
    else :
        print("Your guess is too small. Enter a number that is not", guess)
    chances = chances + 1
if (chances > 5):
    print("You are out of chances :(")