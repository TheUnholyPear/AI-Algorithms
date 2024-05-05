import time

import numpy as np
from matplotlib import pyplot as plt, pyplot
from pandas import read_csv
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

ins_file = 'unsplit_900x5_Shuf_4prior_0_diff_alignDCT_sent_ins.csv'

labs_file = 'unsplit_900x5_Shuf_4prior_0_diff_alignDCT_sent_labs.csv'

# Read inputs and labels
# split into input and output columns
X = read_csv(ins_file, header=None)
y = read_csv(labs_file, header=None)
# split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

frames = 4
features_per_frame = X_train.shape[1] // frames

X_train_reshaped = X_train.to_numpy().reshape((-1, frames, features_per_frame))
X_test_reshaped = X_test.to_numpy().reshape((-1, frames, features_per_frame))


def modelling(X_train, y_train, X_test, y_test):


    # Create model
    model = Sequential()
    model.add(LSTM(23))
    model.add(Dense(56, activation='relu'))
    model.add(Dense(23))

    model.compile(optimizer='adam', loss='mse', metrics=['mse'])

    model.fit(X_train, y_train, epochs=1, batch_size=32, verbose=1)


    visualisation(X_test, y_test, model)

    return model

def visualisation(X_test, y_test, model):
    # Evaluate


    # A fairly simple visualisation, pick 6 at random and compare output to actual
    labelNo = [1500, 5789, 11370, 24, 501, 25999]

    fig = plt.figure()
    for labels in range(0, len(labelNo)):
        # Extrac data and convert to list
        row = X_test.iloc[labelNo[labels], :]
        # Extract the values only as an array and convert
        row = row.values
        row = row.tolist()

        # Predict output
        yhat = model.predict(np.array([row]))

        # Get labels from test set
        lab = y_test.iloc[labelNo[labels], :]

        # Specify plot no
        plotCount = int('3' + '2' + str(labels))

        # Add a subplot covering screen
        ax = fig.add_subplot(plotCount + 1)
        plt.plot(lab)
        plt.plot(yhat[0])
    plt.show()


def extras_view_input_data(X_test, labelNo):
    # Extras, create a figure to look at the input data

    # Extrac data and convert to list
    row = X_test.iloc[labelNo, :]
    # Extract the values only as an array and convert
    row = row.values
    row = row.tolist()

    fig_inps = plt.figure()
    # Add a subplot covering screen
    ax = fig_inps.add_subplot(111)
    # Plot data on subplot
    ax.plot(row)
    # Show on screen6
    plt.show()


def extras_view_label(y_test, labelNo):
    # Display prediction

    lab = y_test.iloc[labelNo, :]
    fig_inps = plt.figure()
    # Add a subplot covering screen
    ax = fig_inps.add_subplot(111)
    # Plot data on subplot
    ax.plot(lab)
    # Show on screen6
    plt.show()


modelling(X_train_reshaped, y_train, X_test_reshaped, y_test)
