def answer_question(user_input, qa_pairs):
    for qa in qa_pairs: #loops through the dictionary and has qa as a variable to substitute for the dictionary quetion
        if user_input.lower() == qa["question"].lower(): #if the user input is equal to the question inside the dictionary it will return the answer in the dictionary
            return qa["answer"]
    return "I don’t know." #if its not inside the dictionary it will return it doenst know

def main():
    qa_pairs = [ #dictionary to hold all the questions and answers as pairs
        {
            "question": "Should you let the steak come to room temperature before cooking?",
            "answer": "Yes, let the steak sit at room temperature for about 30 minutes before cooking to ensure even cooking."
        },
        {
            "question": "How hot should the pan be?",
            "answer": "The pan or grill should be very hot, around 400-450°F (204-232°C), to sear the steak and create a flavorful crust."
        },
        {
            "question": "How do you season a steak before cooking?",
            "answer": "Season the steak generously with salt and pepper on both sides. You can also add garlic powder, onion powder, or fresh herbs like rosemary for extra flavor."
        },
        {
            "question": "How long should you cook the steak on each side?",
            "answer": "For a 1-inch thick steak, cook for about 3-4 minutes on each side for medium-rare. Adjust the time for desired doneness."
        },
        {
            "question": "How can you check the doneness of the steak?",
            "answer": "Use a meat thermometer: 125°F (52°C) for rare, 135°F (57°C) for medium-rare, 145°F (63°C) for medium, 150°F (66°C) for medium-well, and 160°F (71°C) for well-done."
        },
        {
            "question": "Do you need to let the steak rest after cooking?",
            "answer": "Yes, let the steak rest for 5-10 minutes after cooking. This allows the juices to redistribute, making the steak more tender and juicy."
        },
        {
            "question": "What is the best way to cut the steak?",
            "answer": "Slice the steak against the grain, which means cutting across the muscle fibers, to ensure tenderness."
        },
        {
            "question": "Can you use butter or oil for cooking the steak?",
            "answer": "Yes, you can use high smoke point oils like canola or avocado oil. You can also add butter at the end of cooking for extra flavor."
        },
        {
            "question": "What is the most delicious cut of steak?",
            "answer": "I don’t know."
        },
        {
            "question": "Should you flip the steak multiple times while cooking?",
            "answer": "It's best to flip the steak only once during cooking to develop a nice crust on each side."
        }
    ]
    
    while True:
        user_input = input("What are some questions you have about steak? ") #input to ask users
        if user_input.upper() == "STOP": #stop if they say STOP
            break
        answer = answer_question(user_input, qa_pairs) #calls the function so that its able to answer the question with the dictionary and the user input
        print(answer) #print out the answer

main()
