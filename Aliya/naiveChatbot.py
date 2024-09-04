# Machine Learning Foundations
# Period 2
# Assingment 0_3 Naive Python Chatbot\

# Name: Aliya
# Date: 09/01/24


#Questions and answers about pickles
questions = ["What are pickles?", "How are pickles made?", "Where are pickles from?", "What are different kinds of pickles?", "How long do pickles last?", 
             "How healthy are pickles?", "Why are pickles sour?", "Can I make pickles at home?", "Can you pickle fruits?", "What qualities make a good pickle?"]
answers = ["Pickles are traditionally cucumbers that have been preserved in a solution of vinegar, salt, and water. The pickling process extends the shelf life of the vegetable and gives them a sour, tangy flavour.", 
           "To make pickles, cucumbers are soaked in a brine made from water, vinegar, salt, and sometimes sugar and spices. They can be fermented over time or quickly pickled with heat. Fermentation involves naturally occurring bacteria converting sugars into lactic acid, which acts as a preservative.", 
           "Pickles originated in ancient Mesopotamia around 2400BC. Pickles have strong ties with the Jewish community, however, cultures across the globe have utilised pickling as it is synonymous with the process of fermenting vegetables, for instance the kimchi is a traditional fermented vegetable dish in Korea. There is no one place that pickles are from; pickles are a diverse and global food.", 
           "There are many different kinds of pickles within the traditional pickled cucumber and when expanding the pickle to include any and all pickled vegetables. Here is an incomplete list of merely the different variations of pickled cucumbers: bread and butter pickles, cornichons, gherkins, kosher pickles, dill pickles, full sour pickles, and refrigerated pickles.", 
           "Jarred or canned pickles that have been heat processed can last indefinitely if unopened. Once opened, however, pickles can still last for up to two years. Fresh or homemade pickles that have not been pasteurised should be consumed within 75 days of purchase or until the brine is cloudy.", 
           "Pickles have many benefits for gut health, muscle cramps, and blood sugar as they contain numerous vitamins, minerals, prebiotics and antioxidants. However, pickles are high in sodium which can have detrimental health implications for people with high blood pressure, diabetes, or who are generally advised to limit their salt intake.", 
           "Pickles are sour because they are fermented in brine or vinegar, which creates acetic acid and lactic acid that give pickles their salty, sour taste.", 
           "Yes, making pickles at home is simple and fun! You just need fresh cucumbers or another vegetable if you're feeling adventurous, a brine made of vinegar, water, and salt, and any spices you like. You can either ferment them or use the quick pickling method, depending on how much time you have.", 
           "Yes, many fruits can be pickled, including peaches, watermelon rinds, apples, and pears. Pickled fruits can be sweet or savory and are often used as accompaniments to meats, cheeses, or desserts, adding a unique and flavorful twist to various dishes.", 
           "A good pickle is characterised by many qualities: crunchiness, balanced flavour, firmness, aroma, appropriate acidity, appearance, and consistency."]

#Function to returns the correct answer corresponding to the question asked
def getAnswer(question):
    return (answers[questions.index(question)])

#Function to prompt user for a question and return correct answer.
def askQuestion():
    userQuestion = input("Enter your question regarding pickles:")
    while True:
        #Outputs correct answer if question is known
        if userQuestion in questions:
            print(getAnswer(userQuestion))
            userQuestion = input("If you would like to stop enter STOP, otherwise, enter your question regarding pickles:")
        
        #Allows the user to stop the program
        elif userQuestion == "STOP":
            break

        #Prompts the user again if answer to question asked is unknown
        else:
            userQuestion = input("I do not know. Please enter another question regarding pickles. If you would like to stop enter STOP:")

def main():
    #TODO fill out main with calls to your custom functions. Delete 'pass' when done.
    askQuestion()

main()