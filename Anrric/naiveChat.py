def answer_question(user_input, questions, answers):
    for i in range(len(questions)): #loops through the dictionary and has qa as a variable to substitute for the dictionary quetion
        if user_input.lower() == questions[i].lower(): #if the user input is equal to the question inside the dictionary it will return the answer in the dictionary
            return answers[i]
    
    return "I don’t know." #if its not inside the dictionary it will return it doenst know

def main():
    questions = ["Should you let the steak come to room temperature before cooking?", "How hot should the pan be?","How do you season a steak before cooking?","How long should you cook the steak on each side?","How can you check the doneness of the steak?","Do you need to let the steak rest after cooking?","What is the best way to cut the steak?","Can you use butter or oil for cooking the steak?","What is the most delicious cut of steak?", "Should you flip the steak multiple times while cooking?"]
    answers = ["Yes, let the steak sit at room temperature for about 30 minutes before cooking to ensure even cooking.","The pan or grill should be very hot, around 400-450°F (204-232°C), to sear the steak and create a flavorful crust.","Season the steak generously with salt and pepper on both sides. You can also add garlic powder, onion powder, or fresh herbs like rosemary for extra flavor.","For a 1-inch thick steak, cook for about 3-4 minutes on each side for medium-rare. Adjust the time for desired doneness.""Use a meat thermometer: 125°F (52°C) for rare, 135°F (57°C) for medium-rare, 145°F (63°C) for medium, 150°F (66°C) for medium-well, and 160°F (71°C) for well-done.","Yes, let the steak rest for 5-10 minutes after cooking. This allows the juices to redistribute, making the steak more tender and juicy.","Slice the steak against the grain, which means cutting across the muscle fibers, to ensure tenderness.","Yes, you can use high smoke point oils like canola or avocado oil. You can also add butter at the end of cooking for extra flavor.","Which ever one is the fattest.","It's best to flip the steak only once during cooking to develop a nice crust on each side."]
    
    while True:
        user_input = input("What are some questions you have about steak? ") #input to ask users
        if user_input.upper() == "STOP": #stop if they say STOP
            break
        answer = answer_question(user_input, questions, answers) #calls the function so that its able to answer the question with the dictionary and the user input
        print(answer) #print out the answer

main()
