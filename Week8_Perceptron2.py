import numpy as np


class Perceptron(object):

    # ==========================================#
    # The init method is called when an object #
    # is created. It can be used to initialize #
    # the attributes of the class.             #
    # ==========================================#
    def __init__(self, no_inputs, max_iterations=20, learning_rate=0.05):
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
                errors = label - prediction
                self.weights += self.learning_rate * errors * inputs

    def train_batch(self, training_data, labels, batch_size=50):
        assert len(training_data) == len(labels)
        for _ in range(self.max_iterations):
            for batch in range(0, len(training_data), batch_size):
                batch_end = batch + batch_size
                batch_inputs = training_data[batch:batch_end]
                batch_labels = labels[batch:batch_end]

                batch_predictions = [self.predict(inputs) for inputs in batch_inputs]
                errors = np.array(batch_labels) - np.array(batch_predictions)
                weight_adjustment = np.sum([self.learning_rate * errors[i] * batch_inputs[i] for i in range(len(batch_inputs))], axis=0)

                self.weights += weight_adjustment

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
            if prediction == labels[i]:
                results += 1
        if results != 0:
            accuracy = (results / len(testing_data)) * 100
        print("Accuracy:\t" + str(accuracy))
