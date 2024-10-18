# Qlearning example for mini blackjack
import random
import time
import plotly.express as px
import pandas as pd

# -------------- PART 1: Implement Mini blackjack --------------

STATES = [9, 10, 11, 18, 19, 20, 21, 22]
ACTIONS = ["hit", "stand"]
CARDS = [9, 10, 11]

# Handles a single turn of our game
def miniBlackjackTurn(hand):
    # Ask the user to select a new action
    #user_action = input("Do you want to hit or stand: ")
    user_action = random.choice(ACTIONS)

    # If the input is "hit" choose a new card and add the card to the hand
    if user_action == "hit":
        new_card = random.choice(CARDS)
        hand += new_card
        #print("new card:", new_card)

    # If the input is stand, don't add a card
    #print("current hand:", hand)

    # Treat everything above 21 as "bust" which we will represent as 22
    if hand >= 22:
        hand = 22
        #print("You bust!")
    
    return hand, user_action

def playGameEpisode(q_table):
    # Choose a random card
    hand = random.choice(CARDS)
    isPlaying = True
    while isPlaying:
        new_hand, action = miniBlackjackTurn(hand)
        # Update our q table
        reward = computeReward(hand, action)
        updateQTable(q_table, hand, new_hand, reward, action)

        # If we bust or if user chose to stand, then end game
        if new_hand >= 22 or action == "stand":
            isPlaying = False
        hand = new_hand

# -------------- PART 2: Q LEARNING HELPER FUNCTIONS --------------
def computeReward(state, action):
    if action == "stand" and state in [19, 20, 21]:
        return 1
    elif action == "hit" and state >= 18:
        return -1
    elif action == "stand" and state < 19:
        return -1
    else:
        return 0

# Initialize an empty Q table with 8 rows for the states, and 2 columns for the actions
def initializeQTable():
    return [[0,0] for i in range(8)]

# print the Q table
def printTable(q_table):
    print(ACTIONS)
    for i in range(len(q_table)):
        print(str(STATES[i]) + " " + str(q_table[i]))

def updateQTable(q_table, old_hand, new_hand, reward, action):
    # Initializing given constants in equation
    learningRate = 0.1
    discountFactor = 0.4

    # Finding corresponding index in Q table given a state and action
    actionIndex = ACTIONS.index(action)
    oldHandIndex = STATES.index(old_hand)
    newHandIndex = STATES.index(new_hand)

    # Creating other variables in equation
    currentQValue = q_table[oldHandIndex][actionIndex]
    maxFutureReward = max(q_table[newHandIndex][0], q_table[newHandIndex][1])

    # Update Q table with value determined by equation
    newQValue = currentQValue + learningRate*(reward + (discountFactor * maxFutureReward) - currentQValue)
    q_table[oldHandIndex][actionIndex] = newQValue

def initializeDataFrame(q_table):
    main_table = pd.DataFrame(q_table)
    main_table.insert(0, "episode", 0) # for q table data frame inserting at column 0, we are calling it 'episode', and all values are 0
    main_table.insert(0, "states", STATES)
    return main_table

def displayGraphs(main_table):
    figHit = px.scatter(main_table, x = "episode", y = 0, color = "States", title = "Q-Values for Hit") # y=0 means looking at 'hit' column 0, y is states
    figHit.show()
    figStand = px.scatter(main_table, x = "episode", y = 1, color = "States", title = "Q-Values for Stand")
    figStand.show()

# -------------- PART 3: CONDUCT Q LEARNING ON MINI BLACKJACK --------------

def qLearningOnMiniBlackjack():
    q_table = initializeQTable()
    main_table = initializeDataFrame(q_table)
    episodes = 2000

    for i in range(episodes):
        #printTable(q_table)
        playGameEpisode(q_table)

        # Add q tables to the dataFrame which will allow us to visualize the q-values on a graph
        dfQ = pd.DataFrame(q_table)
        dfQ.insert(0, "episode", i)
        dfQ.insert(0, "States", STATES)
        main_table = pd.concat([main_table, dfQ])
        #time.sleep(1)
    displayGraphs(main_table)
    print("Training finished")
    printTable(q_table)

qLearningOnMiniBlackjack()