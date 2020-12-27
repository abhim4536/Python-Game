import random
n = random.randint(1,101)
number_of_guesses = 1

print("You Have Only 10 Chance To Guess The Right Number Try Your Luck")

while number_of_guesses <= 10:
    guesse_number = int(input("Guess The Right Number Between 1 To 100: "))
    if guesse_number > n:
        print("Your Guessing is Too High!")
    elif guesse_number < n:
        print("Your Guessing is Too Low!")
    else:
        print("You Won")
        print("Your Winning Guesses Is", number_of_guesses)
        break
    print(10-number_of_guesses,"Guesses Has Left")
    number_of_guesses += 1


if(number_of_guesses>10):
    print("Game Over,Better Luck Next Time,\n"f"The Hidden Number Is {n}.")

