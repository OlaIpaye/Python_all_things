# welcome message
print("Welcome to my Quiz!")

# Ask user if they want to play
playing = input("Do you want to play my game? ")

if playing != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's get started :)")

#initialize score to keep track of correct answers
score = 0

# ask user multiple questions
answer = input("What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")

answer = input("What is the Capital of Nigeria? ")

if answer.lower() == "abuja":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is abuja.")

answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is central processing unit.")

answer = int(input("How many cities are in England? "))

if answer == 75:
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 75.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
print("Thanks for playing my game!")
# End of the quiz

