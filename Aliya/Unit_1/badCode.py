question1 = "What is the most intelligent animal on Earth?"
q1_answer1 = "Humans"
q1_answer2 = "Dolphins"
q1_answer3 = "Chimpanzees"
q1_answer4 = "Elephants"
question2 = "How many planets are in our solar system?"
q2_answer1 = "7"
q2_answer2 = "8"
q2_answer3 = "9"
q2_answer4 = "10"

letters = ["A", "B", "C", "D"]
answers = ["Humans", "Dolphins", "Chimpanzees", "Elephants"]

def askQuestion(question, answers, correctAnswer):
    print(question)
    for i in range(4):
        print(letters[i] + " " + answers[i])
       
    userAnswer = input("Enter your answer: ")
https://drive.google.com/file/d/1v48ktJoUJA_BelAR-ajve7iVdZBFclX5/view?usp=sharing
    while True:
        if user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer: ")
        elif user_answer == "A":
            print("Correct!")
            break
        else:
            print ("Incorrect! Try again!")
            user_answer = input("Enter your answer: ") 


def main():
    #prints question and answer choices and prompts user to answer
    print(question1)
    print("A)", q1_answer1)
    print("B)", q1_answer2)
    print("C)", q1_answer3)
    print("D)", q1_answer4)
    user_answer = input("Enter your answer: ")
    #addresses if the user's answer is not an answer choice
    '''while useranswer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")'''
    #determines whether the user's answer is correct or incorrect
    while True:
        if user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer: ")
        elif user_answer == "A":
            print("Correct!")
            break
        else:
            print ("Incorrect! Try again!")
            user_answer = input("Enter your answer: ")


    '''if useranswer == "B":
        print("Incorrect!")
    if useranswer == "C":
        print("Incorrect!")
    if useranswer == "D":
        print("Incorrect!")
    if useranswer != "A" and useranswer != "B" and useranswer != "C" and useranswer != "D":
        print("Invalid input. Please enter A, B, C, or D.")'''

    print(question2)
    print("A)", q2_answer1)
    print("B)", q2_answer2)
    print("C)", q2_answer3)
    print("D)", q2_answer4)
    user_answer = input("Enter your answer: ")
    while True:
        if user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer: ")
        elif user_answer == "A":
            print("Correct!")
            break
        else:
            print ("Incorrect! Try again!")
            user_answer = input("Enter your answer: ")

    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        user_answer = input("Enter your answer: ")
    
    if user_answer == "A":
        print("Incorrect!")
    if user_answer == "B":
        print("Correct!")
    if user_answer == "C":
        print("Incorrect!")
    if user_answer == "D":
        print("Incorrect!")
    if user_answer != "A" and user_answer != "B" and user_answer != "C" and user_answer != "D":
        print("Invalid input. Please enter A, B, C, or D.")

main()