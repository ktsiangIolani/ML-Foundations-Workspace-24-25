import random 

def main():
    user1 = input("What is your name? ")
    user2 = input("What is your name? ")

    user1_number = random.randrange(1, 5001) 
    user2_number = random.randrange(1, 5001)

    print(f"{user1}'s score: {user1_number}")
    print(f"{user2}'s score: {user2_number}")

if __name__ == "__main__":
    main()
