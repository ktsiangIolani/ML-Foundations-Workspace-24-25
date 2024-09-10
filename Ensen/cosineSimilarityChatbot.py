# Machine Learning Foundations
# Period 2
# Assingment 0_3 Naive Python Chatbot

# Name: Ensen
# Date: 9/3/24

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = ["Who is the brawler that uses a guitar to attack?", "What brawler throws cards?", "How many rare brawlers are in the game?", "Give me a rare brawler.", "What is El primos title?", "Who is the most recent brawler added to the game?", "Which brawler has a hotdog?", "How many brawlers are in the game?", "How many animal brawlers are in the game?", "Who is the Unicorn brawler?"]
#list for questions
answers = ["Poco", "Tara", "10", "Jacky", "El Luchador", "Moe", "Doug","83", "10", "Berry"]
#list for answers
def similar_function(user_input, question):#acts as a score calculator
    maxScore = 0
    vectorizer = TfidfVectorizer()#creates a vectorizer

    vector = vectorizer.fit_transform([user_input, question])# map our users question and our supported question onto some n dimensional graph
    similarity = cosine_similarity(vector[0:1], vector[1:2])# calcualte the cosine similarity (distance) between the two vectors
    if similarity[0][0] > maxScore:
        maxScore = similarity[0][0]
    return maxScore

def ask_questions(stop):
    while True:

        valid = False

        user_answer = input("Ask a question about Brawl Stars: ")#takes the users input

        for i in range(len(questions)):#a for loop for the length of quesitons
            if similar_function(user_answer, questions[i]) >= .6:#if the return from the function is correct print out the correct answer 
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