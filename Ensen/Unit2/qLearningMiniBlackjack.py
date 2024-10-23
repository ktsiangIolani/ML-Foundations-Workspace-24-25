#Qleraning exmaple for mini blackjack


import random
import time
import plotly.express as px
import pandas as pd
#------------------- Part 1 Implement Mini blackjack -----------------------


STATES = [9, 10, 11, 18, 19, 20, 21, 22]
ACTIONS = ["hit", "stand"]
CARDS = [9, 10, 11]

# handles a single turn of our game
def miniBlackjackTurn(hand):
    #ask the user to select a new action
    action = random.choice(ACTIONS)

    #if the unput is "hit" choose a new card and add the card to the hand
    if action == "hit":
        newCard = random.choice(CARDS)
        hand += newCard
        print("new card: ", newCard)
    
    #if the input is stand, dont' add a card
    print("current hand: ", hand)

    #treat everything above 21 as "bust" which we will represnt as 22
    if hand > 22:
        hand = 22

    return hand, action

def playGameEpisode(qTable):
    #choose a random card
    hand = random.choice(CARDS)
    print("initial hand: ", hand)
    isPlaying = True
    while isPlaying:
        newHand, action = miniBlackjackTurn(hand)
        reward = computeReward(hand, action)
        updateQTable(qTable, hand, newHand, reward, action)
        #update our q table
        #if we bust or if user chose to stand, then end game
        if newHand >= 22 or action == "stand":
            isPlaying = False
        hand = newHand

#------------------ Part 2: Q learning helper functions ---------------------
def computeReward(hand, userInput):
    if userInput == "stand" and hand in [19,20,21]:
        return 1
    
    elif userInput == "hit" and hand > 19:
        return -1
    
    elif userInput == "stand" and hand < 19:
        return -1
    else:
        return 0
    

def initialQTable():
    return [[0,0] for i in range(8)]

def printTable(qTable):
    for i in range(len(qTable)):
        print(qTable[i])

def updateQTable(qTable, oldHand, newHand, reward, action):
    learningRate = 0.1
    discountFactor = 0.8

    actionIndex = ACTIONS.index(action)
    oldHandIndex = STATES.index(oldHand)
    newHandIndex = STATES.index(newHand)

    currentQValue = qTable[oldHandIndex][actionIndex]
    maximumFutureReward = max(qTable[newHandIndex][0], qTable[newHandIndex][1])
    newQValue = currentQValue + learningRate*(reward + discountFactor * maximumFutureReward - currentQValue)
    qTable[oldHandIndex][actionIndex] = newQValue

def initializeDataFrame(qTable):
    mainTable = pd.DataFrame(qTable)
    mainTable.insert(0, "episode", 0)
    mainTable.insert(0, "states", STATES)
    return mainTable

def displayGraphs(mainTable):
    figHit = px.scatter(mainTable, x="episode", y=0, color="states", title="Q-Values for Hit")
    figStand = px.scatter(mainTable, x="episode", y=1, color="states", title="Q-Values for Stand")
    figHit.show()
    figStand.show()

#-------------------------- Part 3 Conduct Q Learning On Mini BlackJack ------------------------
    
def qLearningOnMiniBlackjack():
    qTable = initialQTable()
    mainTable = initializeDataFrame(qTable)
    episodes = 10000

    for i in range(episodes):
        printTable(qTable)
        playGameEpisode(qTable)

        #Add q tables to the dataFrame which will allow us to visualize the q-values on a graph
        dfQ = pd.DataFrame(qTable)
        dfQ.insert(0, "episode", i)
        dfQ.insert(0, "states", STATES)
        mainTable = pd.concat([mainTable, dfQ])
    displayGraphs(mainTable)
    print("training finished")
    printTable(qTable)


qLearningOnMiniBlackjack()