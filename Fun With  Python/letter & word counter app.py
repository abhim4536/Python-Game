print("Welcome to the letter Counter App\n")

name = input("What is your name: ").title().strip()
name = name.capitalize()
print("Hello!", name)

print("I will count the numbr of times that a specific letter occurs in a message.")
message = str(input("\nPlease enter a message: "))
letter = str(input("Which letter would you like to count the occurrences of: "))

message = message.lower()
letter = letter.lower()

number_of_letter = message.count(letter)

mlen = len(message)
print("\n" + name + ",your message has " + str(
    number_of_letter) + " " + letter.capitalize() + "'s in it. And your message has total " + str(mlen) + " words\n")

greet = "Thank You So Much For Using This App."
greet = greet.center(50)
print(greet)
