# Machine Learning Foundations
# Period 2
# Assingment 0_3 Naive Python Chatbot\

# Name: Ethan Mashimo
# Date: 9/2/24

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

def specificMatch(userInput):
    question = False
    for i in range(len(questions)): #loop through questions
        if userInput == questions[i]: #find the index of the question that matches our userInput
            print (answers[i])
            question = True
            break
                    #use that index for get the index of the answer
    if question == False:
        return False
    return True

def similarWords(userInput, questions):
    maxScore = 0
    closestQuestion = ""
    for questions in userInput:
        vectorizer = TfidfVectorizer()

    #map our users question and our supported question onto some n dimensional graph
    vector = vectorizer.fit_transform([userInput, questions])
    #calculate the cosine similarity (distance) between the twp vectors
    similarity = cosine_similarity(vector[0:1], vector[1:2])
    print("Cosine Similarity", similarity[0][0])
    if similarity[0][0] > maxScore:
        maxScore = similarity[0][0]
        closestQuestion = questions
    print("Closest question: ", closestQuestion)
    print("Max Score: ", maxScore)
    return maxScore
    
    return "I don't understand this question."  

def chatbot():
    print("Welcome to my video game chatbot, if you would like to exit just type 'exit'")

    while True:
        
        userInput = input("Write your question or type 'exit' to leave: " )
        
        if specificMatch(userInput) == False:
            answer = similarWords(userInput, questions) #if no questions are the same as the questions in the list use the similar words function
            print(answer)
        
        
        
        if userInput == "exit": #if user types exit then exit the chatbot
            print("Thanks for chatting, cya next time")
            break
    

        
    

        
        

def main():
    chatbot()
    

main()