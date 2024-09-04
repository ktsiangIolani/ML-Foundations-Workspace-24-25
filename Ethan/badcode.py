question1 = "What is the most intelligent animal on Earth?"
q1_answers = ["Humans", "Dolphins", "Chimpanzees", "Elephants"]
question2 = "How many planets are in our solar system?"
q2_answers = ["7", "8", "9", "10"]
letters = ["A", "B", "C", "D"]

def askQuestion(question, answers, correctAnswer):
    print(question)
    for i in range(4):
        print(letters[i] + " " + q2_answers[i])
    useranswer = input("Enter your answer: ")
    while useranswer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")
    if useranswer == ["A", "C", "D"]:
        print("Incorrect")
    if useranswer == "B":
        print("Correct!")
    if useranswer != ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")

def main():
    print(question1)
    for i in range(4):
        print(letters[i] + " " + q1_answers[i])

    useranswer = input("Enter your answer: ")
    while useranswer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")
    if useranswer == "A":
        print("Correct!")
    if useranswer == ["B", "C", "D"]: #made this into a list to simpler it and make it smaller
        print("Incorrect")
    if useranswer != ["A", "B", "C", "D"]: #Original was too long so I shortned it into a list aswell
        print("Invalid input. Please enter A, B, C, or D.")
    print(question2)
    for i in range(4):
        print(letters[i] + " " + q2_answers[i])
    useranswer = input("Enter your answer: ")
    while useranswer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")
    if useranswer == ["A", "C", "D"]:
        print("Incorrect")
    if useranswer == "B":
        print("Correct!")
    if useranswer != ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
main()

