# Qlearning example for mini blackjack
import random

# -------------- PART 1: Implement Mini blackjack --------------

STATES = [9, 10, 11, 18, 19, 20, 21, 22]
ACTIONS = ["hit", "stand"]
CARDS = [9, 10, 11]

# Handles a single turn of our game
def miniBlackjackTurn(hand):
    # Ask the user to select a new action
    user_action = input("Do you want to hit or stand: ")

    # If the input is "hit" choose a new card and add the card to the hand
    if user_action == "hit":
        new_card = random.choice(CARDS)
        hand += new_card
        print("new card:", new_card)

    # If the input is stand, don't add a card
    print("current hand:", hand)

    # Treat everything above 21 as "bust" which we will represent as 22
    if hand >= 22:
        hand = 22
        print("You bust!")
    
    return hand, user_action

def playGameEpisode():
    # Choose a random card
    hand = random.choice(CARDS)
    isPlaying = True
    while isPlaying:
        new_hand, action = miniBlackjackTurn(hand)
        # Update our q table

        # If we bust or if user chose to stand, then end game
        if new_hand >= 22 or action == "stand":
            isPlaying = False
        hand = new_hand

# -------------- PART 2: Q LEARNING HELPER FUNCTIONS --------------
def computeReward(state, action):
    if action == "stand" and state in STATES:
        return 1
    elif action == "hit" and state >= 19:
        return -1
    elif action == "stand" and state < 19:
        return -1
    else:
        return 0

def main():
    # playGameEpisode()
    print(computeReward(20, "hit"))
    print(computeReward(19, "hit"))
    print(computeReward(19, "stand"))
main()