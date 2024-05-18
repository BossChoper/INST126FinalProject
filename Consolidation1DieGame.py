import random
#import pandas as py
import pandas as py
#import numpy as np
import numpy as np

#EXAMPLE PANDAS USAGE
data = {
    'Name': ['Player 1'],
    'Points': [25],
    'Ranking': [1]
}
df = py.DataFrame(data)
print(df)

#Testing document
#In this practice, one player rolls between two numbers

#GLOBAL VARIABLE LIST-----------------------
currentPlayer = 1
#list to store all rolled numbers.
practice_results = []
#test dictionary to store results and organize into categories, preferably per player
practice_dictionary = {1: 0, 2 : 0}
#test save all results total
all_practice_results = {1 : 0}

#testing die is two sided
two_sided_die = (1, 2)
#this is the die the player will set
sided_die = []
#below is to be updated with sided_die in accordance
sided_die_rolls = {}

#turn 1 for player 1
turn = 0
players = []
#append players to the list

#goal to reach to win game for one player
limit_score = 50

#add up total points for turn scoring
total_points = 0

#variable for the odd roll side when comparing
odd_die = 0

#variables keep track of player data
players = []
player_data = {}

#METHOD LIST ----------------------------------
def doRoll(sided_die_rolls):
    temp_results = []
    temp_roll_results = sided_die_rolls
    for index in range(3):
        current_roll = random.choice(sided_die)
        temp_results.append(current_roll)
        #count up the key
        temp_roll_results[current_roll] += 1
    print(temp_results)
    return(temp_results)

def completeRoll(sides):
    #each player rolls three times
    #stores rolls in this list
    temp_results = []
    #stores results in this dict
    temp_roll_results = sided_die_rolls
    #completes a set of rolls for one player
    for index in range(3):
        current_roll = random.choice(sided_die)
        temp_results.append(current_roll)
        temp_roll_results[current_roll] += 1
    print(temp_results)
    checkForTwoRolls
    print("This is what you rolled.")
    if isTupledOut(temp_results) == True:
        print("No points will be added.")
        return 0
    else:
        rerollKeep = int(input("You're safe to reroll or keep points. Enter 1 to reroll, 2 to keep. "))
        if rerollKeep == 1:
            rerollOddDie(temp_results)
            if isTupledOut(temp_results) == True:
                print("No points will be added.")
                return 0
            else:
                print("Rerolled safely. These are your points gained. ")
                print(temp_results)
                addUpPoints(temp_results)
                toAdd = addUpPoints(temp_results)
                #needs to be added to player's scorecard
                #enter exact name of the key
                player_data[f"Player {currentPlayer}"] += toAdd
                printAScore(currentPlayer)

        else:
            print("Kept results. These are your points gained. ")
            addUpPoints(temp_results)
            toAdd = addUpPoints(temp_results)
            #needs to be added to player's scorecard
            #enter exact name of the key
            player_data[f"Player {currentPlayer}"] += toAdd
            # to print out player score print(player_data[f"Player {currentPlayer}"])
            printAScore(currentPlayer)

#initial roll. Rolls all dies and stores in results list/dictionary
def practiceDieRoll():
    #range(3) will roll a die three times and store in the results
    for index in range(3):
        #randomly picks one number from two sided die, between 1 and 2
        current_roll = random.choice(two_sided_die)
        practice_results.append(current_roll)
        #below adds it to the appropriate section in dictionary
        practice_dictionary[current_roll] += 1
    #initial roll results
    print(practice_dictionary)
    print(practice_results)

#checking if two rolls are the same in three
#finished (could be expanded)
def checkForTwoRolls(temp_results):
    if temp_results[0] == temp_results[1] or practice_results[1] == practice_results[2] or practice_results[0] == practice_results[2]:
        print("Two rolls are the same")

#rerolling a die based on which die was found to be different
def rerollOddDie(practice_results):
    #if two rolls are the same, reroll the odd roll
    if practice_results[0] != practice_results[1] and practice_results[0] != practice_results[2]:
        odd_die = 1 #the first number is the odd one out
    elif practice_results[1] != practice_results[0] and practice_results[1] != practice_results[2]:
        odd_die = 2 #the second number is the odd one out
    else:
        odd_die = 3 #the third number is the odd one out

    if odd_die == 1:
        practice_results[0] = random.randint(1,2)
    elif odd_die == 2:
        practice_results[1] = random.randint(1,2)
    else:
        practice_results[2] = random.randint(1,2)


#checking if all rolls are the same
#finished (could be expanded)
def isTupledOut(practice_results):
    if practice_results[0] == practice_results[1] and practice_results[0] == practice_results[2]:
            print("All rolls are the same. Tupled out!")
            return True
    else:
        return False
            #take away points, no points will be added


#confirmation of final results
print(practice_dictionary)
print(practice_results)


#adds all numbers together in current roll results
#needs to be finished
def addUpPoints(practice_results):
    points = 0
    for int in practice_results:
        points += int
    print(points)
    return points

#checks if any players rearched 50 points or game is over five turns
#needs to be finished
def isGameOver():
    if total_points == limit_score:
         print("Game Over")

#ends game at the fifth turn
#finished
def endFiveTurns():
    #ends game if this is the end of the fifth turn
    if turn == 5:
        print("Alright, game is over.")

#shows current score for all players when called
#needs to be tested
def displayScore():
    checkDisplayInterest = int(input("Do you want to see all player scores? Enter 1 for yes, 2 for no: "))
    if checkDisplayInterest == 1:
         printAllPlayerInfo()
    else:
        print("Okay, keep playing. ")

#keeps track of who has highest score
#needs to be finished
def getHighestScore():
    highest = max(player_data.values())
    win_player = max(player_data, key = player_data.get)
    return highest


#changes number of sides to roll
#finished
def changeDieSides(sides):
    #sides = int(input("Enter a number: "))
    for side in range(1, sides + 1):
        sided_die.append(side)
        add_side = {side: 0}
        #adds side to the roll dictionary
        sided_die_rolls.update(add_side)
    #both variables should have the same sides
    print(sided_die)
    print(sided_die_rolls)
    return sided_die, sided_die_rolls

#updates player count.
def changePlayerCount(playerCount):
    
    for player in range(1, playerCount+1):
        key = f"Player {player}"
        players.append(player)
        player_data[key] = 0
    print(players)
    print(player_data)
    return players, player_data

#print each player's name in the list one by one
#finished
def printAScore(currentPlayer):
    score = f"Player {currentPlayer}"
    print(f"{player_data[score]} is your score.")

#print out each player and their associated items
#needs to be tested
def printAllPlayerInfo():
    for player in range(1, playerCount + 1):
        #side1Points, side2Points, side3Points = points
        #need to take key and associated item and print them out for each player
        #print(f"{player} got {side1Points} for one side, {side2Points} for second side, {side3Points} for third side")
        #print(player)
        printPlayer = player_data[f"Player {player}"]
        print(f"{printPlayer} is the appropriate score for Player: {player}")
    
    #Added a dataframe to display player scores
    data = {
    'Name': ['Player 1'],
    'Points': [25],
    'Ranking': [1]
    }
    df = py.DataFrame(player_data, index=[0])
    print(df)
    
    
    
#testing: player dictionary
def testData():
    player_data = {"Player 1": (0, 1, 2),
                   "Player 2": (0, 1, 2)}
    player_data["Player 1"]
    player_data.keys()

#Testing: a full program for the game
print("Hello, welcome to TupledOut.")

#Method to set die sides
sides = int(input("Give an integer for the die sides: "))
changeDieSides(sides)
#returned sided_die, sided_die_rolls

#Method to set player count
playerCount = int(input("Give an integer for player count: "))
changePlayerCount(playerCount)
#returned players, player_data

#while loop till all turns are reached
#turn = 0 at beginning, endFiveTurns = 5
while turn != 5:
    currentPlayer = 1
    #making a while loop to repeat rolls until all players are done.
    while currentPlayer != playerCount + 1:
        #Beginning first rolls
        print("Thank you. Let's start our first rolls with Player: " f"{currentPlayer}")
        turn += 1
        completeRoll(sides)

        #This is for checking your current score at the end of your turn
        checkCurrentPoints = int(input("Do you want to see your own current score? Enter 1 for yes, 2 for no: "))
        if checkCurrentPoints == 1:
            printAScore(currentPlayer)
        else:
            print("Okay, we won't. Continue to next player.")

        #Move to next player
        currentPlayer += 1
        print("Nice. Moved to next player! ")
    #This is for the end of a turn.
    displayScore()
    turn += 1
    if turn == 4 or max(player_data) == 50:
        endFiveTurns()
        print("The player that won is... ")
        printAllPlayerInfo()
        winning_player = max(player_data, key=data.get)
        print(winning_player)
        repeatGame = int(input("Do you want to play again? Enter 1 for yes, 2 for no: "))
        if repeatGame == 1:
            print("Okay, go again!")
            print("------ NEW GAME -----")
            turn == 0
        else:
            print("Okay, good game!")

