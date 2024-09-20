# Machine Learning Foundations
# Period 2
# Assingment 0_3 Naive Python Chatbot

# Name: Ensen
# Date: 9/3/24

questions = ["Who is the brawler that uses a guitar to attack?", "What brawler throws cards?", "How many rare brawlers are in the game?", "Give me a rare brawler.", "What is El primos title?", "Who is the most recent brawler added to the game?", "Which brawler has a hotdog?", "How many brawlers are in the game?", "How many animal brawlers are in the game?", "Who is the Unicorn brawler?"]
#list for questions
answers = ["Poco", "Tara", "10", "Jacky", "El Luchador", "Moe", "Doug","83", "10", "Berry"]
#list for answers
def similar_function(user_input, question):#acts as a score calculator
    user_words = set(user_input.lower().split())#changes the uesrs input into a list with each index being a differnt word all being lowercase
    question_words = set(question.lower().split())#same thing for the questions
    similar_words = user_words & question_words#looks at both list and extracts the similar words and makes a new list
    return len(similar_words) / len(question_words) >= .5#looks to see if what was inputted has a good score and returns that number

def ask_questions(stop):
    while True:

        valid = False

        user_answer = input("Ask a question about Brawl Stars: ")#takes the users input

        for i in range(len(questions)):#a for loop for the length of quesitons
            if similar_function(user_answer, questions[i]):#if the return from the function is correct print out the correct answer 
               print(answers[i])#prints the answer
               valid = True

        if valid == False:
            print("Invalid input, try again.")
        
        user_stop = input("Type (STOP) to stop: ")
        if user_stop == stop:
            exit()
def main():
    ask_questions("STOP")    
main()