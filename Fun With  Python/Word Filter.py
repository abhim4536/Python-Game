from better_profanity import profanity
profanity.load_censor_words()

text=input("Enter Your Word To Censor:")
correct=profanity.censor(text,"*")
print(correct)