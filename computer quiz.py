print("Welcome to my Computer Quiz!")

#create a variable and use  input function for the user to start typing...
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does FIFA stand for? ")
if answer.lower() == "federation internationale de football association":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the President of America? ")
if answer.lower() == "joe biden":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital city of New York? ")
if answer.lower() == "albany":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) *100) + "%.")

