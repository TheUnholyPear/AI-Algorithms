import numpy as np


class Perceptron(object):

    # ==========================================#
    # The init method is called when an object #
    # is created. It can be used to initialize #
    # the attributes of the class.             #
    # ==========================================#
    def __init__(self, no_inputs, max_iterations=20, learning_rate=0.1):
        self.no_inputs = no_inputs
        self.weights = np.ones(no_inputs) / no_inputs
        self.max_iterations = max_iterations
        self.learning_rate = learning_rate

    # =======================================#
    # Prints the details of the perceptron. #
    # =======================================#
    def print_details(self):
        print("No. inputs:\t" + str(self.no_inputs))
        print("Max iterations:\t" + str(self.max_iterations))
        print("Learning rate:\t" + str(self.learning_rate))

    # =========================================#
    # Performs feed-forward prediction on one #
    # set of inputs.                          #
    # =========================================#
    def predict(self, inputs):
        dot_product = np.dot(inputs, self.weights)
        return 1 if dot_product > 0 else 0

    # ======================================#
    # Trains the perceptron using labelled #
    # training data.                       #
    # ======================================#
    def train(self, training_data, labels):
        assert len(training_data) == len(labels)
        for _ in range(self.max_iterations):
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights += self.learning_rate * error * inputs
            print(str(self.weights))

    # =========================================#
    # Tests the prediction on each element of #
    # the testing data.
    # =========================================#
    def test(self, testing_data, labels):
        results = 0
        accuracy = 0.0
        assert len(testing_data) == len(labels)
        for i in range(len(testing_data)):
            prediction = self.predict(testing_data[i])
            print("actual: " + str(prediction) + " estimate: " + str(labels[i]))
            if prediction == labels[i]:
                results += 1

        if results != 0:
            accuracy = (results / len(testing_data)) * 100
        print("Accuracy:\t" + str(accuracy))


