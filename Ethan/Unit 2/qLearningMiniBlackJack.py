# example for Q learning with mini black jack
import random
import time
import plotly.express as px
import pandas as pd
# ---------------------- Part 1 Implement Mini blackjack

States = [9, 10, 11, 18, 19, 20, 21, 22]
Actions = ["hit", "stand"]
CARDS = [9, 10, 11]

#handles a single turn of our game
def miniBlackjackTurn(hand):
    #ask the user to select a new action
    # userInput = input("choose hit or stand: ")

    userInput = random.choice(Actions)

    # if the input is "hit" choose a new card and add the card to the hand 

    if userInput == "hit":
        total = random.choice(CARDS)
        hand += total
        print("new card: ", total)
   # if the input is stand, dont add a card
    print("current hand: ", hand)

    # treat everything above 21 as "bust" whcih we will represent as 22
    if hand > 22: 
        hand = 22

    return hand, userInput

def playGameEpisode(q_table):
    # choose a random card
    hand = random.choice(CARDS)
    print("initial hand: ", hand)
    isPlaying = True
    while isPlaying:
        new_hand, userInput = miniBlackjackTurn(hand)
        # update our Q table
        reward = computeReward(hand, userInput)
        updateQTable(q_table, hand, new_hand, reward, userInput)
        

        # if we bust or if user chose to stand, then end game
        if new_hand >= 22 or userInput == "stand":
            isPlaying = False
        hand = new_hand

# ------------------------- PART2: Q LEARNING HELPER FUNCTIONS -----------------------------------

def computeReward(hand, userInput):
    if userInput == "stand" and hand in [19, 20, 21]:
        return 1
    elif userInput == "hit" and hand > 17:
        return -1
    elif userInput == "stand" and hand < 19:
        return -1
    else: 
        return 0

def updateQTable(q_table, old_hand, new_hand, reward, action):
    learningRate = 0.1
    discountFactor = 0.9

    actionIndex = Actions.index(action)
    oldHandIndex = States.index(old_hand)
    newHandIndex = States.index(new_hand)

    currentQValue = q_table[oldHandIndex][actionIndex]
    maximumFutureReward = max(q_table[newHandIndex][0], q_table[newHandIndex][1])

    newQ = currentQValue + learningRate * (discountFactor*maximumFutureReward + reward - currentQValue)

    q_table[oldHandIndex][actionIndex] = newQ

def initializeQTable():
    return [[0,0] for i in range(8)]

def printTable(q_table):
    print(Actions)
    for i in range(len(q_table)):
        print(str(States[i])+ " " + str(q_table[i]))

def initDataFrame(q_table):
    main_table = pd.DataFrame(q_table)
    main_table.insert(0, "episode", 0)
    main_table.insert(0,"States", States)

def display_graphs(main_table):
    figHit = px.scatter(main_table, x ="episode", y=0, color="States", title="Q Values for Hit")
    figStand = px.scatter(main_table, x="episode", y=1, color="States", title="Q Values for Stand")
    figHit.show()
    figStand.show()
#---------------------------PART 3------------------------------------

def qLearningOnMiniBlackjack():
    q_table = initializeQTable()
    episodes = 10000
    main_table = initDataFrame(q_table)

    for i in range(episodes):
        printTable(q_table)
        playGameEpisode(q_table)
        # Add q tables to the data which will allow us to visualize the q values
        dfQ = pd.DataFrame(q_table)
        dfQ.insert(0, "episode", i)
        dfQ.insert(0, "States", States)
        main_table = pd.concat([main_table, dfQ])

    display_graphs(main_table)
        # time.sleep(0.5)
    print("Training finished")
    printTable(q_table)

qLearningOnMiniBlackjack()

        
    
   