# ML Foundations
# Perceptron 

# Name:
# Purpose of Perceptron (ie what decision is it making):

# TODO 0 Define variables inputs, bias and activation
inputs = ["Is it currently late?", "Do I have a lot of work to do tonight?", "Am I tired?"]
weights = [-5, 3, 4]
bias = 0.4
activation = lambda x: max(x, 0)

def perceptron():
	# TODO 1 Ask the user to answer questions in the inputs array
	# Store each answer in the array answers (use .append to add a new item to the array)
    answers = []
    for q in inputs:
        answers.append(int(input(q)))

	# TODO 2 Compute a score based on answers, weights and inputs
	# Recall that the score is the sum of every answer multiplied by it's wieght,
	# multiplied by the bias and then passed through the activation function
    sum = 0
    for i in range(len(answers)):
        sum += answers[i]*weights[i]

	# TODO 3 Print out and return the final score
    score = activation(sum * bias)
    return score


# TODO 4 Call your function perceptron.
# If the score is above 0, print out what the user should do if the answer is yes
if perceptron() > 0:
    print("Take a nap")

# Otherwise, print out what the user should do if the answer is no
else:
    print("Stay awake")