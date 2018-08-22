score = 0

print("Please enter T for true and F for false for each questions")

qOne = input ("1. Affordable housing positively affects property values.")

if qOne == "T":
    print("Correct!")
    score = score + 1
elif qOne == "F":
    print("Incorrect.")
else:
    print("Invalid answer.")

qTwo = input ("2. Affordable housing does not increase crime.")
if qTwo == "T":
    print("Correct!")
    score = score + 1
else:
    print("Invalid answer.")

qThree = input ("3. Access to affordable housing is a solution to homelessness.")
if qThree == "T":
    print("Correct!")
    score = score + 1
else:
    print("Invalid answer.")

if score == 3:
    print("Congradulation! You scored a " + str(score) + " on your test.")
else:
    print("You scored a " + str(score) + " on your test. Try again!")

while score != 3:
    score = 0
    qOne = input ("1. Affordable housing positively affects property values.")
    if qOne == "T":
        print("Correct!")
        score = score + 1
    elif qOne == "F":
        print("Incorrect.")
    else:
        print("Invalid answer.")

    qTwo = input ("2. Affordable housing does not increase crime.")
    if qTwo == "T":
        print("Correct!")
        score = score + 1
    elif qTwo == "F":
        print("Incorrect.")
    else:
        print("Invalid answer.")

    qThree = input ("3. Access to affordable housing is a solution to homelessness.")
    if qThree == "T":
        print("Correct!")
        score = score + 1
    elif qThree == "F":
        print("Incorrect.")
    else:
        print("Invalid answer.")

    if score == 3:
        print("Congradulation! You scored a " + str(score) + " on your test.")
    else:
        print("You scored a " + str(score) + " on your test. Try again!")
