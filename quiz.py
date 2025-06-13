# welcome message
print("Welcome to my Quiz!")

# Ask user if they want to play
playing = input("Do you want to play my game? ")

if playing != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's get started :)")

# ask user another question
answer = input("What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct!")
else:
    print("Incorrect! The correct answer is paris.")

answer = input("What is the Capital of Nigeria? ")

if answer.lower() == "abuja":
    print("Correct!")
else:
    print("Incorrect! The correct answer is abuja.")

answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect! The correct answer is central processing unit.")

answer = int(input("How many cities are in England? "))

if answer == 75:
    print("Correct!")
else:
    print("Incorrect! The correct answer is 75.")

