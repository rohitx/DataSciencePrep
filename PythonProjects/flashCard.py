"""
Idea: https://openhatch.org/wiki/Flash_card_challenge

Project: Write a flash card quizzer from scratch


Steps to take:
1. Read in the csv file
2. Randomly pick state and ask the capital
3. Check the answer with the csv file
   if it is correct: go on to the next capital
   if not correct: say incorrect and give the answer
4. Exit the game with the exit key

"""
import pandas as pd
import random

file = "capitals.csv"
head_names = ["state", "capital"]
df = pd.read_csv(file, names=head_names)

# Now start the quiz:
print "Welcome to the game of American state capital!"
print ""
print "*" * 80
count = 0
wrong_answers = []
while count < 50:
    index = random.randint(0, 49)
    state = df.ix[index][0]
    capital = df.ix[index][1]
    answer = str(raw_input("What is the capital of " + state + "? "))
    if answer.lower() == capital.lower():
        print "Correct!"
        print " "
    elif answer == "exit":
        print "You got wrong answers to these states: "
        for state in wrong_answers:
            print state
        print "GoodBye"
        break
    else:
        print "Incorrect. The correct answer is " + capital
        print " "
        if state not in wrong_answers:
            wrong_answers.append(state)
    count += 1
