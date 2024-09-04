# Machine Learning Foundations
# Period 2
# Assingment 0_3 Naive Python Chatbot\

# Name: Ethan Mashimo
# Date: 9/2/24

questions = ["How should I start video games?", 
             "What kind of genre of video games are there?", 
             "Do you believe video games are educational?", 
             "What do I need to play video games?",
             "What is your favorite video game of all time?",
             "What is your favorite video game genre?",
             "Do you prefer single-player or multiplayer games?",
             "What type of gaming device do you prefer: PC, console, or mobile?",
             "Are video games bad for you?",
             "What do you think the next big trend in gaming will be?",
             ]
answers = ["Maybe you should start with a Nintendo Switch or begin with a computer as not many games require a beefed-out computer.",
           "There are a lot of video game genres out there starting with action, adventure, role-playing, simulation, strategy, sports, puzzle, horror, and even more. Each offers unique experiences.",
           "Yes, as I believe they can teach important lessons like problem-solving or good hand-eye coordination",
           "You can play video games on a phone or just choose to get a gaming device such as a computer.",
           "My favorite game of all time is Minecraft and that's because that was the first game introduced to me and it just a classic for me",
           "I would say my favorite genre is adventure games where you can work with friends",
           "I prefer multiplayer but I don't mind single-player. Multiplayer allows you to play with friends.",
           "I prefer the PC, as many of the games I play are on my computer.",
           "Unless you are playing an overdramatic amount of video games, I don't believe that video games are bad for you",
           "Me personally I think the next big trend will be like new virtual reality things.",
           ]

def displayQuestion(questions):
    print("Question: " + questions)

def displayAnswer(answer):
    print("Answer: " + answer)

def chatbot():
    print("Welcome to my video game chatbot, if you would like to exit just type 'exit' ")

    while True:
        for i, question in enumerate(questions, 1):
            print(str(i) + ". " + question)
        userInput = input("Your choice from 1-10 or exit:")

        if userInput == "exit":
            print("Thanks for chatting, cya next time")
            break
        if userInput.isdigit():
            choice = int(userInput)
            if 1 <= choice <= 10:
                displayQuestion(questions[choice - 1])
                displayAnswer(answers[choice - 1])
                
                # Wait for the user to type 'next'
                while True:
                    nextInput = input("Type 'next' to continue or 'exit' to quit: ").lower()
                    if nextInput == "next":
                        break
                    elif nextInput == "exit":
                        print("Thanks for chatting, cya next time")
                        return
                    else:
                        print("Please type 'next' to continue or 'exit' to quit.")
            else:
                print("Please choose a valid number between 1 and 10.")
        else:
            print("Please enter a number between 1 and 10, or type 'exit'.")

        

def main():
    chatbot()
    

main()