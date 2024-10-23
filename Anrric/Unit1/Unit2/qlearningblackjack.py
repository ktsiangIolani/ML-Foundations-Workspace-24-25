#Example algorithm for Q learning for Mini BlackJack 
import random
import time
import plotly.express as px
import pandas as pd
#----------------------- Part 1 Implement Mini BlackJack  ----------------------

STATES = [9,10,11,18,19,20,21, 22]
ACTION = ["hit", "stand"]
CARDS = [9,10,11]
# handles a single turn of our game 
def miniBlackjackTurn(hand):
    #ask the user to select a new action 
    user_input = random.choice(ACTION)
    
    #if the input is "hit" choose a new card and add the card to the hand 
    if user_input == "hit":
        choiceCards = random.choice(CARDS)
        hand += choiceCards
        print("new card:", choiceCards)
    #if input is stand, dont add a card 
    print("your current hand", hand)
    #treat everything above 21 as bust which we will rrepresent as 22 
    if hand > 22:
        hand = 22 
    
    return hand, user_input

def playGameEpisode(q_table):
    # choose a random card 
    hand = random.choice(CARDS)
    print("initial hand:", hand)
    isPlaying = True 
    while isPlaying:
        newHand,action = miniBlackjackTurn(hand)
        # update our q table 
        reward = computeReward(hand,action )
        updateQtable(hand, newHand, reward, q_table, action)

        #if we bust or if user chose to stand, then end game 
        if newHand >= 22 or action == "stand":
            isPlaying = False
        hand = newHand
    



#------------Part 2: Q Learning Helper Functions ----------------
def computeReward(hand, user_input):
    #first case 
    if user_input == "stand" and hand in [19, 20, 21]:
        return 1 
    elif user_input == "hit" and hand > 19:
        return -1
    elif user_input == "stand" and hand < 19:
        return -1 
    else:
        return 0 
    
def initializeQTable():
    return [[0,0] for i in range(8)]

def printTable(q_table):
    for i in range(len(q_table)):
        print(q_table[i])

def updateQtable(old_hand, new_hand,reward, q_table, action):
    learningRate = 0.1
    discountFactor = 0.4

    actionIndex = ACTION.index(action)
    oldhandIndex = STATES.index(old_hand)
    newhandIndex = STATES.index(new_hand)

    currentQvalue = q_table[oldhandIndex] [actionIndex]
    maximumFutureReward = max(q_table[newhandIndex][0], q_table[newhandIndex][1])
    newQvalue = currentQvalue + learningRate * (reward + discountFactor * maximumFutureReward - currentQvalue)
    q_table[oldhandIndex][actionIndex] = newQvalue

def initializeDataFrame(q_table):
    main_table = pd.DataFrame(q_table)
    main_table.insert(0,"episode",0)
    main_table.insert(0,"states", STATES)
    return main_table

def displayGraphs(main_table):
    figHit = px.scatter(main_table, x="episode", y=0, color="states", title="Q-Values for Hit")
    figStand = px.scatter(main_table, x="episode", y=1, color="states", title = "Q-Values for Stand")
    figHit.show()
    figStand.show()

    #-----------------------------------------Part 3 CONDUCT Q LEARNING ON MINI BLACKJACK -------------------------------
def qLearningOnMiniBlackJack():
    q_table = initializeQTable()
    main_table = initializeDataFrame(q_table)
    episodes = 10000
    for i in range(episodes):
        printTable(q_table)
        playGameEpisode(q_table)
        dfQ = pd.DataFrame(q_table)
        dfQ.insert(0,"episode", i)
        dfQ.insert(0, "states", STATES)
        main_table = pd.concat([main_table,dfQ])
    displayGraphs(main_table)
    print("Training Finished")
    printTable(q_table)
    
    


qLearningOnMiniBlackJack()
    
    

    

        


    