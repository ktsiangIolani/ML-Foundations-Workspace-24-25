import random 

def main():
    user1 = input("What is your name?")
    user2 = input("what is your name?")

    user1_number = random.randrange(1,5000)
    user2_number = random.randrange(1,5000)
    
    print("user1 score" + user1_number)
    print("")
    print("user2 score:" + user2_number)


main()