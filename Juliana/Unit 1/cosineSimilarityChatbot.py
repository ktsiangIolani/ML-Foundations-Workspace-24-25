# Machine Learning Foundations
# Period 2
# Assingment 0_3 Cosine Similarity Chatbot
# Name: Juliana
# Date: 9/2/24

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = ["What is Xiaolongbao?", "Where do Xiaolongbao originate from?", "How do you eat Xiaolongbao?", "What do you dip  Xiaolongbao in?","What meat is in Xiaolongbao?", "What is the soup inside made out of?", "How do you cook Xiaolongbao?", "How many folds do Xiaolongbao have when wrapping them?", "Where can I find authentic Xiaolongbao?", "What is your favorite food?"]
answers = ["They are chinese soup filled dumplings!", "Changzhou", "You take a nibble of the wrapper, and let the soup pour into your spoon. Then, you enjoy the soup. Finally, you dip the Xiaolongbao in your vinegar and enjoy!", "Black vinegar. Lots of places also add slivers of ginger in the sauce!", "Pork", "It is made out of an aspic that contains the gelatin from either pork skin or bones. The gelatin-like mixture will melt into a delicious broth when the Xiaolongbao is steamed!", "It is usually steamed in a bamboo steamer!", "At least 18 folds!", "In China, of course! In the U.S., however, Din Tai Fung is oftentimes a popular place to eat Xiaolongbao.", "Xiaolongbao!"]

def split_words(text):
    return text.lower().split()

def match_question(user_answer, questions):
    maxScore = 0
    closestQuestion = ""
    for question in questions:
        vectorizer = TfidfVectorizer() #creates a vectoizer

        # map our users questiona nd our supported questiononto some n dimenstional graph
        vector = vectorizer.fit_transform([user_answer, question]) 
        # caculate the cosine similarity (distance) between the two vectors
        similarity = cosine_similarity(vector[0:1], vector[1:2]) 
        if similarity[0][0] > maxScore:
            maxScore = similarity[0][0]
            closestQuestion = question
    return closestQuestion
        

def main():
    #allows the program to repeat
    while True:
        user_answer = input("Ask me questions about Xiaolongbao! ") #Prompts user to ask a question
        if user_answer == ("STOP"): #if the user wants to stop
            print("Bye!") #chatbot says bye
            break #exits program
        
        matched_question = match_question(user_answer, questions) 

        if matched_question: #checks if the user's answer is one of the valid questions
            index = questions.index(matched_question) #finds the index of the question in the questions array
            print(answers[index]) #prints the corresponding index in the answers array
        else: #if the user doesn't ask a valid question
            print("enter a valid question please!") #prints this
       
main()
