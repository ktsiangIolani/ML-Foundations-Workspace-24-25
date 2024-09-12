question1 = "What is the most intelligent animal on Earth?"
answerA = "Humans"
answerB = "Dolphins"
answerC = "Chimpanzees"
answerD = "Elephants"
question2 = "How many planets are in our solar system?"
answer1 = "7"
answer2 = "8"
answer3 = "9"
answer4 = "10"
def main():
    print(question1)
    print("A)", answerA)
    print("B)", answerB)
    print("C)", answerC)
    print("D)", answerD)
    useranswer = input("Enter your answer: ")
    while useranswer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")
    if useranswer == "A":
        print("Correct!")
    if useranswer == "B":
        print("Incorrect!")
    if useranswer == "C":
        print("Incorrect!")
    if useranswer == "D":
        print("Incorrect!")
    if useranswer != "A" and useranswer != "B" and useranswer != "C" and useranswer != "D":
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")
    print(question2)
    print("A)", answer1)
    print("B)", answer2)
    print("C)", answer3)
    print("D)", answer4)
    useranswer = input("Enter your answer: ")
    while useranswer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")

    if useranswer == "A":
        print("Incorrect!")
    if useranswer == "B":
        print("Correct!")
    if useranswer == "C":
        print("Incorrect!")
    if useranswer == "D":
        print("Incorrect!")
    if useranswer != "A" and useranswer != "B" and useranswer != "C" and useranswer != "D":
        print("Invalid input. Please enter A, B, C, or D.")
        useranswer = input("Enter your answer: ")
main()
