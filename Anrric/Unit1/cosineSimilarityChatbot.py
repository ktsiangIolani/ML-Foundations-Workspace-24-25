from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
questions = ["Should you let the steak come to room temperature before cooking?", "Is steak healthy?","What is a steak?","How long should you cook the steak on each side?","How can you check the doneness of the steak?","Do you need to let the steak rest after cooking?","What is the best way to cut the steak?","Can you use butter or oil for cooking the steak?","What is the most delicious cut of steak?", "Should you flip the steak multiple times while cooking?"]
answers = ["Yes, let the steak sit at room temperature for about 30 minutes before cooking to ensure even cooking.","Steak can be healthy because it has alot of protein.","A steak is a thick cut of meat from a cow","Season the steak generously with salt and pepper on both sides. You can also add garlic powder, onion powder, or fresh herbs like rosemary for extra flavor.","For a 1-inch thick steak, cook for about 3-4 minutes on each side for medium-rare. Adjust the time for desired doneness.""Use a meat thermometer: 125°F (52°C) for rare, 135°F (57°C) for medium-rare, 145°F (63°C) for medium, 150°F (66°C) for medium-well, and 160°F (71°C) for well-done.","Yes, let the steak rest for 5-10 minutes after cooking. This allows the juices to redistribute, making the steak more tender and juicy.","Slice the steak against the grain, which means cutting across the muscle fibers, to ensure tenderness.","Yes, you can use high smoke point oils like canola or avocado oil. You can also add butter at the end of cooking for extra flavor.","Which ever one is the fattest.","It's best to flip the steak only once during cooking to develop a nice crust on each side."]


def findSimilarQuestion(userQuestion):
    maxScore = 0
    closestQuestion = ""
    for question in questions:
        vectorizer = TfidfVectorizer() #creates a vectorizer
        vector = vectorizer.fit_transform([userQuestion,question]) #map our users question and our supported question onto some n dimentional graph
        similarity = cosine_similarity(vector[0:1],vector[1:2]) #calculate the cosine similarity (distance) between the two vectors
        print("Cosine Similarity", similarity[0][0])
        if similarity[0][0] > maxScore:
            maxScore = similarity[0][0]
            closestQuestion = question
    print("Closest question:", closestQuestion)
    print("max:",maxScore)
    return maxScore




def main(): #holds the questions and answers in lists 
    while True: #makes it so that its continuous
        user_input = input("what are your questions about cooking a steak? ") #user input to find what the user wants to know about
        final_answer = findSimilarQuestion(user_input)#calls in the final_algo function and uses the input to then loop through and find the match value compared to the questions. If the match value is the highest in one of the questions, then it would become the accurate_match which then would become the answers[i]
        print(final_answer) #print the final answer and respond to the user
        



main()
            
        
        