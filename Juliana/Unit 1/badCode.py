
choices = ["A)", "B)", "C)", "D)"]
question1 = "What is the most intelligent animal on Earth?"
answers1 = ["Humans", "Dolphins", "Chimpanzees", "Elephants"]


question2 = "How many planets are in our solar system?"
answers2 = ["7", "8", "9", "10"]


def askQuestion(question, answers, correctAnswer):
    print(question)
    for i in range(4):
        print(choices[i] + " " + answers[i])

    user_answer = input("Enter your answer: ")
    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")
    
    if user_answer == correctAnswer:
        print("Correct!")
    elif user_answer not in choices:
        print("Invalid input. Please enter A, B, C, or D.")
    else:
        print("Incorrect!")

def main():
    askQuestion(question1, answers1, "A")
    askQuestion(question2, answers2, "B")
main()
