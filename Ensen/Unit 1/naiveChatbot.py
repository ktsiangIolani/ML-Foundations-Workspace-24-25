letters = ["A","B","C","D"]

question = "Who is the brawler that uses a guitar to attack?" 
answer1 = ["Poco", "Leon", "Carl", "Tick"]#A

question2 = "What brawler throws cards?"
answer2 = ["Frank", "Tara", "Bibi", "Byron"]#B

question3 = "How many rare brawlers are in the game?"
answer3 = ["13", "16", "10", "8"]#C

question4 ="Which is a rare brawler?"
answer4 = ["Jacky", "Melodie", "Mico", "Draco"]#A

question5 = "What is El primos title?"
answer5 = ["El Luchador", "One With Nature", "El Mariachi", "Boom!"]#A

question6 = "Who is the most recent brawler added to the game?"
answer6 = ["Lilly", "Draco", "Moe", "Clancy"]#C

question7 = "Which brawler has a hotdog?"
answer7 = ["Mr.P", "Otis", "Doug", "Kit"]#C

question8 = "How many brawlers are in the game?"
answer8 = ["81", "82", "83", "84"]#C

question9 = "How many animal brawlers are in the game?"
answer9 = ["9", "10", "5", "12"]#B

question10 = "Who is the Unicorn brawler?"
answer10 = ["Berry", "Colette", "Barley", "Emz"]#A


def ask_question(question, answer, correct_answer, stop):
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
    user_stop = input("Type (STOP) if you want to stop if not type anything: ")
    if user_stop == stop:
        False
        exit()         

def main():
    while True:
        ask_question(question, answer1, "A", "STOP")
        ask_question(question2, answer2, "B", "STOP")
        ask_question(question3, answer3, "C", "STOP")
        ask_question(question4, answer4, "A", "STOP")
        ask_question(question5, answer5, "A", "STOP")
        ask_question(question6, answer6, "C", "STOP")
        ask_question(question7, answer7, "C", "STOP")
        ask_question(question8, answer8, "C", "STOP")
        ask_question(question9, answer9, "B", "STOP")
        ask_question(question10, answer10, "A", "STOP")
main()
