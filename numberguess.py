print("=======Number Guessing Agent=======")
print("Think number between 1 to 100")


low = 0
high = 100
attemps = 0

while low <= high :

    guess = (low + high) // 2
    attemps += 1

    print("\n My guess is: ", guess)

    feedback = input("Enter C (correct), H (too high), L (too low): ").upper()

    if feedback == 'C':
        print("I guess your number!!!!")
        print("Total attemps:", attemps)
        break

    elif feedback == 'H':
        high = guess - 1

    elif feedback == 'L':
        low = guess + 1

    else:
        print("Invalid feedback! Try again.")

else:
    print("Your feedback seems inconsistent !")
