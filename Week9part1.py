import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

data_path = "./"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

# Dataset preparation
train_input = np.array([np.array(d[1:]) for d in train_data])
# Separating the labels from the image
train_label = np.array([int(d[0]) for d in train_data])

test_input = np.array([np.array(d[1:]) for d in test_data])
# Separating the labels from the image
test_label = np.array([int(d[0]) for d in test_data])


def modelling(train_input, train_label, test_input, test_label):
    # All model work should be submitted in this function
    # THis includes creation, training, evaluation etc.

    # normalizing
    train_input = train_input / 255.0
    test_input = test_input / 255.0

    # determine the number of input features
    n_features = train_input.shape[1]

    # Create model
    model = Sequential()

    model.add(Dense(64, activation='relu', input_shape=(n_features,)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    opt = SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='SparseCategoricalCrossentropy', metrics=['accuracy'])

    model.summary()

    model.fit(train_input, train_label, epochs=5, batch_size=32, verbose=1)

    loss, acc = model.evaluate(test_input, test_label, verbose=0)

    print('Test Accuracy: %.3f' % (acc * 100))

    visualisation(test_input, test_label, model)

    # Return model at end
    return model


def visualisation(test_input, test_label, model):
    labelchoice = np.random.randint(0, test_input.shape[0])
    predictLabel = test_label[labelchoice]

    predictData = np.array(test_input[labelchoice])[None, ...]

    # make prediction
    yhat = model.predict(predictData)

    predicted_class = np.argmax(yhat)
    predicted_prob = np.max(yhat) * 100

    print(f"Actual: {predictLabel}, Predicted: {predicted_class} (Prob: {predicted_prob:.3f})")

    plt.imshow(predictData.reshape(28, 28))
    plt.title(f'Actual: {predictLabel}, Predicted: {predicted_class}')
    plt.show()

    # Display prediction
    yhat = model.predict(predictData)
    print('Predicted: %s (class=%d)' % (yhat, np.argmax(yhat)))
    plt.plot(yhat[0])
    plt.show()


def part1():
    modelling(train_input, train_label, test_input, test_label)


part1()
