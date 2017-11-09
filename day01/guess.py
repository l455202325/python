__author__ = "ZiXing"

age_of_oldboy = 56

type = True

while type:
    you_guess = int(input("guess  age:"))
    if age_of_oldboy == you_guess:
        print("Yes !")
        type = False
    elif age_of_oldboy > you_guess:
        print("you guess is small")

    else:
        print("You guess is old")
