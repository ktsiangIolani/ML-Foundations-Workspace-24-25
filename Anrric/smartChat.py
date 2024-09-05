def better_characters(text): #better characters function is able to have the variable text and I created a punctuation variable so that it would look through each character in text and if there is a punctuation then we would skip it however if there isnt a punctuation then add that letter to clean_text. This then would allow the sentnece to be clean of punctuation making it easier to spllit later on
    text = text.lower()
    punctuations = ",.!:;'"
    clean_text = ""
    for char in text:
        if char not in punctuations:
            clean_text = clean_text + char
    return clean_text

def similarity_char(input_words, sample_words):# this function acts as a similarity score creator
    match = 0
    for char in input_words:# by setting the match to 0 in the beginning, for every char in the input that matches the question (sample_words) it will add 1 to the match variable
        if char in sample_words:
            match = match + 1 
    return match 

def split_words(text): #makes it easier for me to split the words
    return text.split()

def final_algo(user_input, questions, answers): #the final algorithm that uses the better_character function to remove punctuation and makes it lowercase 
    better_input = better_characters(user_input)
    split_input = split_words(better_input) #split words so that it would create a list with each individual word in each element of that list 
    high_score = 0 #base score would be 0
    accurate_match = None #set the variable for the most accurate score
    for i in range(len(questions)): #loops through the array questions that store all my questions in each index
        better_questions = better_characters(questions[i]) #removes punctuation and makes the question lowercased. I used i in the questions that it would follow the for loop
        split_questions = split_words(better_questions) #split the better questions so that each word is a element
        similarity_final = similarity_char(split_input,split_questions) #call the similarity_char function to find the match 
        if similarity_final > high_score:# if the match of the input os higher than 0 (the beginning)
            high_score = similarity_final #then the high score would be the new similarity_final
            accurate_match = answers[i]  #the most accurate match within the question would be based on the i in the for loop
    return accurate_match if accurate_match else "I dont know!" #however if its not an answer, it would respond that it doesnt know

def main(): #holds the questions and answers in lists 
    questions = ["Should you let the steak come to room temperature before cooking?", "Is steak healthy?","What is a steak?","How long should you cook the steak on each side?","How can you check the doneness of the steak?","Do you need to let the steak rest after cooking?","What is the best way to cut the steak?","Can you use butter or oil for cooking the steak?","What is the most delicious cut of steak?", "Should you flip the steak multiple times while cooking?"]
    answers = ["Yes, let the steak sit at room temperature for about 30 minutes before cooking to ensure even cooking.","Steak can be healthy because it has alot of protein.","A steak is a thick cut of meat from a cow","Season the steak generously with salt and pepper on both sides. You can also add garlic powder, onion powder, or fresh herbs like rosemary for extra flavor.","For a 1-inch thick steak, cook for about 3-4 minutes on each side for medium-rare. Adjust the time for desired doneness.""Use a meat thermometer: 125°F (52°C) for rare, 135°F (57°C) for medium-rare, 145°F (63°C) for medium, 150°F (66°C) for medium-well, and 160°F (71°C) for well-done.","Yes, let the steak rest for 5-10 minutes after cooking. This allows the juices to redistribute, making the steak more tender and juicy.","Slice the steak against the grain, which means cutting across the muscle fibers, to ensure tenderness.","Yes, you can use high smoke point oils like canola or avocado oil. You can also add butter at the end of cooking for extra flavor.","Which ever one is the fattest.","It's best to flip the steak only once during cooking to develop a nice crust on each side."]
    while True: #makes it so that its continuous
        user_input = input("what are your questions about cooking a steak? ") #user input to find what the user wants to know about
        final_answer = final_algo(user_input, questions, answers)#calls in the final_algo function and uses the input to then loop through and find the match value compared to the questions. If the match value is the highest in one of the questions, then it would become the accurate_match which then would become the answers[i]
        print(final_answer) #print the final answer and respond to the user




main()
            
        
        