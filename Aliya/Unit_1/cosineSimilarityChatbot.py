# Machine Learning Foundations
# Period 2
# Assingment 0_3 Naive Python Chatbot\

# Name: Aliya
# Date: 09/05/24

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Questions and answers about pickles
questions = ["How long does it take to make pickles?", "How to make pickles?", "Where are pickles from?", "What are different types of pickles?", "Why do pickles last for such a long time?", 
             "How healthy are pickles?", "Why are pickles sour?", "Can I make pickles at home?", "Can you pickle fruit?", "What qualities make a good pickle?"]
answers = ["Pickles can take as short as a day or as long as a month to make, depending on what they are submerged in and the desired outcome.", 
           "To make pickles, cucumbers are soaked in a brine made from water, vinegar, salt, and sometimes sugar and spices. They can be fermented over time or quickly pickled with heat. Fermentation involves naturally occurring bacteria converting sugars into lactic acid, which acts as a preservative.", 
           "Pickles originated in ancient Mesopotamia around 2400BC. Pickles have strong ties with the Jewish community, however, cultures across the globe have utilised pickling as it is synonymous with the process of fermenting vegetables, for instance the kimchi is a traditional fermented vegetable dish in Korea. There is no one place that pickles are from; pickles are a diverse and global food.", 
           "There are many different kinds of pickles within the traditional pickled cucumber and when expanding the pickle to include any and all pickled vegetables. Here is an incomplete list of merely the different variations of pickled cucumbers: bread and butter pickles, cornichons, gherkins, kosher pickles, dill pickles, full sour pickles, and refrigerated pickles.", 
           "Unopened canned or jarred pickles can last indefinitely, as long as they are properly sealed. Pickles undergo the process of fermentation as they are soaked in brine which allows them to last longer on the shelf.", 
           "Pickles have many benefits for gut health, muscle cramps, and blood sugar as they contain numerous vitamins, minerals, prebiotics and antioxidants. However, pickles are high in sodium which can have detrimental health implications for people with high blood pressure, diabetes, or who are generally advised to limit their salt intake.", 
           "Pickles are sour because they are fermented in brine or vinegar, which creates acetic acid and lactic acid that give pickles their salty, sour taste.", 
           "Yes, making pickles at home is simple and fun! You just need fresh cucumbers or another vegetable if you're feeling adventurous, a brine made of vinegar, water, and salt, and any spices you like. You can either ferment them or use the quick pickling method, depending on how much time you have.", 
           "Yes, many fruits can be pickled, including peaches, watermelon rinds, apples, and pears. Pickled fruits can be sweet or savory and are often used as accompaniments to meats, cheeses, or desserts, adding a unique and flavorful twist to various dishes.", 
           "A good pickle is characterised by many qualities: crunchiness, balanced flavour, firmness, aroma, appropriate acidity, appearance, and consistency."]

#Function to distill any question to its key words
def distillWords(sentence):
    extraWords = ["is", "it", "I", "you", "a", "do", "to", "there", "does", "one", "the", "and", "of", "in", "on", "with", "pickles", "are"] #List of common words
    punctuation = ["?", ",", ".", ":", ";", "'s", "'d"] #List of punctuation and contractions
    sentence = sentence.lower()
    for p in punctuation:
        sentence = sentence.replace(p, '') #Removes punctuation and contractions from the given sentence
    sentence = sentence.split(" ")
    for word in sentence:
        if word in extraWords:
            sentence.remove(word) #Removes common words from the given sentence
    return sentence


def findSimilarQuestion(userQ):
    maxScore = 0
    closestQuestion = ""
    for question in questions:
        vectorizer = TfidfVectorizer() #creates a vectorizer

        # map our users question and our supported question onto some n dimensional graph
        vector = vectorizer.fit_transform([userQ, question]) 
        # calculate the cosine similarity (distance) between the two vectors
        similarity = cosine_similarity(vector[0:1], vector[1:2])
        print(similarity)
        if similarity[0][0] > maxScore:
            maxScore = similarity[0][0]
            closestQuestion = question
    #print("Closest question: ", closestQuestion, "\nMax cosine similarity: ", maxScore)
    if maxScore > 0.5:
        return closestQuestion


    '''#List to keep track of what the key words are in each question
    distilledQuestions = []

    #Goes through each question to identify their key words
    for referenceQ in questions: 
        distilledQuestions.append(distillWords(referenceQ)) #Adds the question, distilled down to its key words, to the list 'distilledQuestions'

    #Distills the user's question to its key words
    userQ = distillWords(userQ)

    sharedWordsCount = [] #List of number of shared words in each question
    
    #Goes through all questions, comparing to the user's, and counts the words in common
    for q in distilledQuestions:
        count = 0 
        #Calls function checking the main question word, so only questions with the same main question word get checked further
        for keyWord in q: 
            if keyWord in userQ: #Compares each key word in the given questions to each word in the user's question
                count += 1 #Adds 1 to the count of shared words whenever a key word for the question is found in the user's question
        sharedWordsCount.append(count) #Adds the number of shared words in the question to the list 'sharedWordsCount'
    
    return sharedWordsCount'''


#Function to prompt user for a question and return correct answer.
def askQuestion():
    userQuestion = input("Enter your question regarding pickles:")

    while True:
        question = findSimilarQuestion(userQuestion)
        if question is not None:
            print(answers[questions.index(question)])
            userQuestion = input("If you would like to stop enter STOP, otherwise, enter your question regarding pickles:")
        elif userQuestion == "STOP" or userQuestion == "stop":
            print("Goodbye!")
            break
        else:
            userQuestion = input("I do not know. Please enter another question regarding pickles. If you would like to stop enter STOP:")
        
        '''score = findSimilarQuestion(userQuestion)
        #Outputs the corresponding answer for which question the user's question has the greatest number of shared key words with
        if not score.count(max(score)) > 1:
            print(answers[score.index(max(score))])
            userQuestion = input("\nIf you would like to stop enter STOP, otherwise, enter your question regarding pickles:")
        
        #Allows the user to stop the program
        elif userQuestion == "STOP" or userQuestion == "stop":
            print("\nGoodbye!")
            break

        #Prompts the user again if user's question doesn't have a strong enough correlation, 2 or more words in common, with any given question
        elif all(x < 2 for x in score):
            userQuestion = input("\nI do not know. Please enter another question regarding pickles. If you would like to stop enter STOP:")   

        #Prompts the user again if question asked is not recognized or answer is unknown
        else:
            userQuestion = input("I do not know. Please enter another question regarding pickles. If you would like to stop enter STOP:")
'''
  

def main():
    #TODO fill out main with calls to your custom functions. Delete 'pass' when done.
    findSimilarQuestion("Why do pickles taste sour?")
    #askQuestion()
    
main()


###TRASH
'''
#Questions and answers about pickles
questions = ["How long does it take to make pickles?", "How to make pickles?", "Where are pickles from?", "What are different types of pickles?", "Why do pickles last for such a long time?", 
             "How healthy are pickles?", "Why are pickles sour?", "Can I make pickles at home?", "Can you pickle fruit?", "What qualities make a good pickle?"]
answers = ["Pickles can take as short as a day or as long as a month to make, depending on what they are submerged in and the desired outcome.", 
           "To make pickles, cucumbers are soaked in a brine made from water, vinegar, salt, and sometimes sugar and spices. They can be fermented over time or quickly pickled with heat. Fermentation involves naturally occurring bacteria converting sugars into lactic acid, which acts as a preservative.", 
           "Pickles originated in ancient Mesopotamia around 2400BC. Pickles have strong ties with the Jewish community, however, cultures across the globe have utilised pickling as it is synonymous with the process of fermenting vegetables, for instance the kimchi is a traditional fermented vegetable dish in Korea. There is no one place that pickles are from; pickles are a diverse and global food.", 
           "There are many different kinds of pickles within the traditional pickled cucumber and when expanding the pickle to include any and all pickled vegetables. Here is an incomplete list of merely the different variations of pickled cucumbers: bread and butter pickles, cornichons, gherkins, kosher pickles, dill pickles, full sour pickles, and refrigerated pickles.", 
           "Unopened canned or jarred pickles can last indefinitely, as long as they are properly sealed. Pickles undergo the process of fermentation as they are soaked in brine which allows them to last longer on the shelf.", 
           "Pickles have many benefits for gut health, muscle cramps, and blood sugar as they contain numerous vitamins, minerals, prebiotics and antioxidants. However, pickles are high in sodium which can have detrimental health implications for people with high blood pressure, diabetes, or who are generally advised to limit their salt intake.", 
           "Pickles are sour because they are fermented in brine or vinegar, which creates acetic acid and lactic acid that give pickles their salty, sour taste.", 
           "Yes, making pickles at home is simple and fun! You just need fresh cucumbers or another vegetable if you're feeling adventurous, a brine made of vinegar, water, and salt, and any spices you like. You can either ferment them or use the quick pickling method, depending on how much time you have.", 
           "Yes, many fruits can be pickled, including peaches, watermelon rinds, apples, and pears. Pickled fruits can be sweet or savory and are often used as accompaniments to meats, cheeses, or desserts, adding a unique and flavorful twist to various dishes.", 
           "A good pickle is characterised by many qualities: crunchiness, balanced flavour, firmness, aroma, appropriate acidity, appearance, and consistency."]

def askQuestion():
    userQuestion = input("Enter your question regarding pickles:")

    while True:
        if userQuestion in questions:
'''