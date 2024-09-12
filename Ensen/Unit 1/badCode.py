letters = ["A","B","C","D"]
question = "What is the most intelligent animal on Earth?"
question2 = "How many planets are in our solar system"
answer = ["Humans", "Dolphins", "Chimpanzees", "Elephants"]
answer2 = ["7","8","9","10"]

def ask_question(question, answer, correct_answer):
    print(question)
    for i in range(4):
        print(letters[i] + " " + answer[i])

    user_answer = input("Enter your answer: ")
    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        user_answer = input("Enter your answer: ")

    if user_answer == correct_answer:
        print("Correct!")
    elif user_answer not in letters:
        print("Invalid input. Please enter A, B, C, or D.")
    else:
        print("Incorrect!")

def main():
    ask_question(question,answer, "A")
    ask_question(question2, answer2, "B")
main()