#computer quiz mini game 
print("Welcome to the Computer Quiz!")

start_question = input("Are you ready to start the game? YES/NO: ")

if start_question.upper != "YES":
    quit 

print("Lets Play")
score = 0
answer = input("What is the first day of the work week ")
if answer.lower() == "monday":
    print("That is correct")
    score += 1
else :
    print("That is incorrect")

answer = input("What is the second month of the year? ")
if answer.lower() == "february":
    print("That is correct")
    score += 1
else :
    print("That is incorrect")
answer = input("What is the capital of Ghana? ")
if answer.lower() == "accra":
    print("That is correct")
    score += 1
else:
    print("That is incorrect")

answer = input("Who is the ceo of Apple? ")
if answer.lower()== "tim cook":
    print("That is correct")
    score += 1
else:
    print("That is incorrect")

answer = input("Who won the 2022 world cup? ")
if answer.lower() == "argentina":
    print("That is correct")
    score += 1
else :
    print("That is incorrect")

answer = input("What is the name of the largest planet in our solar sysytem? ")
if answer.lower() == "jupiter":
    print("That is correct")
    score += 1
else :
    print("That is incorrect")

print("Your score is " + str(score))
 

