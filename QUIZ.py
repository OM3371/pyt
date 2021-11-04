print("Welcome to my computer quiz!")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()

print("Okay then! Let's play :)" )
score = 0

answer = input("What does CPU stand for? ")

if answer == "Central Processing Unit":
    print('That is absolutely correct!')
    score = score+1
else:
    print("Sorry! That is incorrect")
    
answer = input("What does GPU stand for? ")

if answer == "Graphics Processing Unit":
    print('That is absolutely correct!')
    score += 1
else:
    print("Sorry! That is incorrect")

answer = input("What does RAM stand for? ")

if answer == "Random Access Memory":
    print('That is absolutely correct!')
    score += 1
else:
    print("Sorry! That is incorrect")

answer = input("What does PSU stand for? ")

if answer == "Power supply":
    print('That is absolutely correct!')
    score += 1
else:
    print("Sorry! That is incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
