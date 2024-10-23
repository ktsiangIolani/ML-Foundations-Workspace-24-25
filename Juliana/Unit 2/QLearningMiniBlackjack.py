# Qlearning example for mini blackjack
import random
import time
import plotly.express as px
import pandas as pd

# ------------------------ Part 1 Implement Mini blackjack --------------------------

STATES = [9, 10, 11, 18, 19, 20, 21, 22]
ACTIONS = ["hit","stand"]
CARDS = [9,10,11]

# handles a single turn of our game
def miniBlackjackTurn(hand):
    # ask the user to select a new action
    user_input = random.choice(ACTIONS)

    # if the input is "hit" choose a new card and add the card to the hand
    if user_input == "hit":
        new_card = random.choice(CARDS)
        hand = hand + new_card
        print("new_card:", new_card)

    # if the input is stand, don't add a card
    print("current hand:", hand)

    # treat everything above 21 as bust which we will represent as 22
    if hand > 22:
        hand = 22

    return hand, user_input

def playGameEpisode(q_table):
    # choose a random card
    hand = random.choice(CARDS)
    print("initial hand: ", hand)
    isPlaying = True
    while isPlaying:
        new_hand, action = miniBlackjackTurn(hand)
        # update our q table
        reward = computeReward(hand, action)
        updateQTable(q_table, hand, new_hand, reward, action)
        # if we bust or if user chose to stand, then end game
        if hand >= 22 or action == "stand":
            isPlaying = False
        hand = new_hand


# ---------------- PART2: Q LEARNING HELPER FUNCTIONS ----------------------
def computeReward(hand, user_input):
    if user_input == "stand" and hand in [19,20,21]:
        return 1
    elif user_input == "hit" and hand >= 18:
        return -1
    elif user_input == "stand" and hand < 19:
        return -1
    else:
        return 0

def initializeQTable():
    return [[0,0] for i in range(8)]

def printTable(q_table):
    print(ACTIONS)
    for i in range(len(q_table)):
        print(str(STATES[i])+ " " + str(q_table[i]))
        
def updateQTable(q_table, old_hand, new_hand, reward, action):
    learningRate = 0.1
    discountFactor = .8

    actionIndex = ACTIONS.index(action)
    oldHandIndex = STATES.index(old_hand)
    newHandIndex = STATES.index(new_hand)

    currentQvalue = q_table[oldHandIndex][actionIndex]
    maximumFutureReward = max(q_table[newHandIndex][0], q_table[newHandIndex][1])

    newQvalue = currentQvalue + learningRate*(reward + discountFactor*maximumFutureReward - currentQvalue)

    q_table[oldHandIndex][actionIndex] = newQvalue

def initializeDataFrame(q_table):
    main_table = pd.DataFrame(q_table)
    main_table.insert(0, "episode", 0)
    main_table.insert(0, "states", STATES)
    return main_table

def displayGraphs(main_table):
    figHit = px.scatter(main_table, x = "episode", y = 0, color = "states", title = "Q-Values for Hit")
    figStand = px.scatter(main_table, x = "episode", y = 1, color = "states", title = "Q-Values for Stand")
    figHit.show()
    figStand.show()


#------------ PART 3 CONDUCT Q LEARNING ON MINI BLACKJACK -----------------

def qLearningonMiniBlackjack():
    q_table = initializeQTable()
    main_table = initializeDataFrame(q_table)
    episodes = 10000

    for i in range(episodes):
        printTable(q_table)
        playGameEpisode(q_table)

        #add q tables to the dataFrame which will allow us to visualize the q-values on a graph
        dfQ = pd.DataFrame(q_table)
        dfQ.insert(0, "episode", i)
        dfQ.insert(0, "states", STATES)
        main_table = pd.concat([main_table, dfQ])

    displayGraphs(main_table)
    print("Training finished")
    printTable(q_table)

qLearningonMiniBlackjack()

    
    

