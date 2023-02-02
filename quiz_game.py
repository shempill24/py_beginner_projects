print("Welcome to my quiz!")

playing = input("Do you want to play a game? ")
if playing.lower() != "yes":
  quit()
  
print("Okay! Let's begin")
score = 0
affirmation = ("are right", "rock", "can't be stopped", "have superior CS knowledge", "are amazing","have a perfect score")
wrong_message = "Sorry, that is incorrect. Your score is {}".format(score)
correct_message = "You {}!".format(affirmation[score])
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    score += 1
    print("You {}! Your current score is {}".format(affirmation[score-1], str(score)))
else:
    print("Sorry, that is incorrect. Your score is {}".format(score))

answer = input("What does LAN stand for? ")
if answer.lower() == "local area network":
    score += 1
    print("You {}! Your current score is {}".format(affirmation[score-1], str(score)))
else:
    print("Sorry, that is incorrect. Your score is {}".format(score))
    
answer = input("What is the two digit numeric system, that only uses 0 and 1, that computers operate using? ")
if answer.lower() == "binary":
    score += 1
    print("You {}! Your current score is {}".format(affirmation[score-1], str(score)))
else:
    print("Sorry, that is incorrect. Your score is {}".format(score))

answer = input("What does 'WWW' stand for? ")
if answer.lower() == "world wide web":
    score += 1
    print("You {}! Your current score is {}".format(affirmation[score-1], str(score)))
else:
    print("Sorry, that is incorrect. Your score is {}".format(score))
    
answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    score += 1
    print("You {}! Your current score is {}".format(affirmation[score-1], str(score)))
else:
    print("Sorry, that is incorrect. Your score is {}".format(score))
    
answer = input("What is an error, flaw or fault in a computer program or system, that causes it to produce an incorrect or unexpected result, or behave in unintendedways called? ")
if answer.lower() == "bug":
    score += 1
    print("You {}! Your current score is {}".format(affirmation[score-1], str(score)))
else:
    print("Sorry, that is incorrect. Your score is {}".format(score))
    
print("You got " + str(score) + " questions correct!")
print("You got " + str(int((score/6)*100)) + "% correct")