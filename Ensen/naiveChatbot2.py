# Machine Learning Foundations
# Period 2
# Assingment 0_3 Naive Python Chatbot

# Name: Ensen
# Date: 9/3/24

questions = ["Who is the brawler that uses a guitar to attack?", "What brawler throws cards?", "How many rare brawlers are in the game?", "Give me a rare brawler?", "What is El primos title?", "Who is the most recent brawler added to the game?", "Which brawler has a hotdog?", "How many brawlers are in the game?", "How many animal brawlers are in the game?", "Who is the Unicorn brawler?"]
answers = ["Poco", "Tara", "10", "Jacky", "El Luchador", "Moe", "Doug","83", "10", "Berry"]


def ask_questions(stop):
    while True:
        user_answer = input("Ask a question about Brawl Stars: ")
        if user_answer not in questions:
            print("Invalid input try again")
        for i in range(len(questions)):
            if user_answer == questions[i]:
                print (answers[i])
        user_stop = input("Type (STOP) to stop: ")
        if user_stop == stop:
            exit()
def main():
    ask_questions("STOP")    
main()