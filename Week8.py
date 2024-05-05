import matplotlib.pyplot as plt
import numpy as np

from Week8_Perceptron1 import Perceptron as Perceptron1
from Week8_Perceptron2 import Perceptron as Perceptron2

data_path = "./"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")


def part1OR(no_inputs=3):
    P = Perceptron1(no_inputs)
    logic_input = [np.array([1, 0, 0]), np.array([1, 0, 1]), np.array([1, 1, 0]), np.array([1, 1, 1])]
    logic_label = [0, 1, 1, 1]

    P.print_details()
    P.test(logic_input, logic_label)
    P.train(logic_input, logic_label)
    P.test(logic_input, logic_label)


def part1NOT(no_inputs=2):
    P = Perceptron1(no_inputs)
    logic_input = [np.array([1, 0]), np.array([1, 1])]
    logic_label = [0, 1]

    P.print_details()
    P.test(logic_input, logic_label)
    P.train(logic_input, logic_label)
    P.test(logic_input, logic_label)


def part1AND(no_inputs=3):
    P = Perceptron1(no_inputs)
    logic_input = [np.array([1, 0, 0]), np.array([1, 0, 1]), np.array([1, 1, 0]), np.array([1, 1, 1])]
    logic_label = [0, 0, 0, 1]

    P.print_details()
    P.test(logic_input, logic_label)
    P.train(logic_input, logic_label)
    P.test(logic_input, logic_label)


def part1XOR(no_inputs=3):
    P = Perceptron1(no_inputs)
    logic_input = [np.array([1, 0, 0]), np.array([1, 0, 1]), np.array([1, 1, 0]), np.array([1, 1, 1])]
    logic_label = [0, 1, 1, 0]

    P.print_details()
    P.test(logic_input, logic_label)
    P.train(logic_input, logic_label)
    P.test(logic_input, logic_label)


def shape(P, num):
    data = P.weights[1:].reshape(28, 28)
    plt.imshow(data)
    plt.title(f"Perceptron Weight Visualization of {str(num)}")
    plt.show()


def part2(no_inputs=785):
    P = Perceptron2(no_inputs)

    target_digit = 7

    train_input = [np.append([1], d[1:]) for d in train_data]  # Adding bias term
    train_label = [int(d[0] == target_digit) for d in train_data]  # Target digit labels

    test_input = [np.append([1], d[1:]) for d in test_data]  # Adding bias term
    test_label = [int(d[0] == target_digit) for d in test_data]  # Target digit labels

    print("Testing Before for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)

    print("Training for digit:  " + str(target_digit))
    P.train(train_input, train_label)

    print("Testing After for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)


def part2select(num, no_inputs=785):
    P = Perceptron2(no_inputs)

    target_digit = num

    train_input = [np.append([1], d[1:]) for d in train_data]  # Adding bias term
    train_label = [int(d[0] == target_digit) for d in train_data]  # Target digit labels

    test_input = [np.append([1], d[1:]) for d in test_data]  # Adding bias term
    test_label = [int(d[0] == target_digit) for d in test_data]  # Target digit labels

    print("Testing Before for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)

    print("Training for digit:  " + str(target_digit))
    P.train(train_input, train_label)

    print("Testing After for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)


def part2ALL(no_inputs=785):
    P = [Perceptron2(no_inputs) for _ in range(10)]

    for num in range(10):
        train_input = [np.append([1], d[1:]) for d in train_data]  # Adding bias term
        train_label = [int(d[0] == num) for d in train_data]  # Target digit labels

        test_label = [int(d[0] == num) for d in test_data]
        test_input = [np.append([1], d[1:]) for d in test_data]

        print("Testing Before for digit: " + str(num))
        shape(P[num], num)
        P[num].test(test_input, test_label)

        print("Training for digit:  " + str(num))
        P[num].train(train_input, train_label)

        print("Testing After for digit: " + str(num))
        shape(P[num], num)
        P[num].test(test_input, test_label)


def part3(no_inputs=785):
    P = Perceptron2(no_inputs)

    target_digit = 7

    train_input = [np.append([1], d[1:]) for d in train_data]  # Adding bias term
    train_label = [int(d[0] == target_digit) for d in train_data]  # Target digit labels

    test_input = [np.append([1], d[1:]) for d in test_data]  # Adding bias term
    test_label = [int(d[0] == target_digit) for d in test_data]  # Target digit labels

    print("Testing Before for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)

    print("Training for digit:  " + str(target_digit))
    P.train_batch(train_input, train_label)

    print("Testing After for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)


def part3select(num, no_inputs=785):
    P = Perceptron2(no_inputs)

    target_digit = num

    train_input = [np.append([1], d[1:]) for d in train_data]  # Adding bias term
    train_label = [int(d[0] == target_digit) for d in train_data]  # Target digit labels

    test_input = [np.append([1], d[1:]) for d in test_data]  # Adding bias term
    test_label = [int(d[0] == target_digit) for d in test_data]  # Target digit labels

    print("Testing Before for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)

    print("Training for digit:  " + str(target_digit))
    P.train_batch(train_input, train_label)

    print("Testing After for digit: " + str(target_digit))
    shape(P, target_digit)
    P.test(test_input, test_label)


def part3ALL(no_inputs=785):
    P = [Perceptron2(no_inputs) for _ in range(10)]

    for num in range(10):
        train_input = [np.append([1], d[1:]) for d in train_data]  # Adding bias term
        train_label = [int(d[0] == num) for d in train_data]  # Target digit labels

        test_label = [int(d[0] == num) for d in test_data]
        test_input = [np.append([1], d[1:]) for d in test_data]

        print("Testing Before for digit: " + str(num))
        shape(P[num], num)
        P[num].test(test_input, test_label)

        print("Training for digit:  " + str(num))
        P[num].train_batch(train_input, train_label)

        print("Testing After for digit: " + str(num))
        shape(P[num], num)
        P[num].test(test_input, test_label)


if __name__ == "__main__":
    part1AND()
    # part1OR()
    # part1NOT()
    #part1XOR()
    # part2()
    # part2select(8)
    # part2ALL()
    # part3()
    # part3select(8)
    # part3ALL()

