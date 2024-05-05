import random
import time
import math


# Main function to run game
def Nim():
    # initial variables
    initialState = []
    state = ()

    print("Let's play Nim")

    # Add try catch to ensure only valid values are accepted
    valid = False
    while not valid:
        try:
            # Get piles and sticks
            numPiles = input("How many piles initially? ")
            maxSticks = input("Maximum number of sticks? ")

            # Create initial state
            for i in range(int(numPiles)):
                # Use random numbers to generate random number of sticks
                sticks = random.randint(1, int(maxSticks))
                initialState.append(sticks)

            # set first or second go and create state
            print("The intial state is " + str(initialState))
            print("Do you want to play a) first or b) second")
            turn = input("Enter a or b")
            if (str(turn).lower() == "a"):
                state = (initialState, 1)  # user is always MAX player
                valid = True

            elif (str(turn).lower() == "b"):
                state = (initialState, 2)  # AI is always MIN player
                valid = True

            else:
                raise ValueError("Invalid Input")
        except ValueError:
            print("invalid input, please re-enter")
            initialState = []  # reset interstate foe invalid input

    return state


# THe user turn, let them choose
def userturn(state):
    # Next states called here (import from your own code)
    succ = nextstates(state)

    # if only an empty state left, pick the stick and return
    if (len(succ) == 1 and succ[0][0] == [1]):
        print("Only one stick left, and you picked it up")
        return succ[0]
    if (len(succ) == 1 and succ[0][0] == []):
        print("You picked up the last stick!")
        return succ[0]
    # Print list of moves
    print("Next move options:")
    for i in range(len(succ)):
        print(str(i) + ".    " + str(succ[i][0]))
    while True:  # Loop until valid input
        try:
            moveIndex = input("Enter next move option number: ")
            if 0 <= int(moveIndex) < len(succ):
                print("You moved to state " + str(succ[int(moveIndex)][0]) + "\n")
                return succ[int(moveIndex)]
            else:
                print("invalid input, please re-enter")
        except ValueError:
            print("Invalid input, enter a number")  # Input is not a number


# Given a state, start the game
def game_begin(state):
    game_state = state
    mem.clear()

    print("\ngame start ", game_state)
    # while no winner, keep alternating
    while game_state[0] != []:

        # You will need to create your own AI function
        if (game_state[1] == 1):
            print("Your turn")
            game_state = (userturn(game_state)[0], 2)
            # game_state = AI_player_basic(game_state)
        else:
            print("AI's turn")
            game_state = AI_player_basic(game_state)
            print("AI moved to state " + str(game_state[0]) + "\n")
        # game_state = AI_player_basic(game_state)
        print("new state is", str(game_state))

    # if final state is 1, 2 wins
    if (game_state[1] == 2):
        print("win for player 2 (AI)")
    else:
        print("You win! (Player)")


mem = {}


def AI_player_basic(state):
    if state[0]:
        if state[1] == 2:
            stateLists = (min_value_prune(state, float('-inf'), float('inf')))[0]
            return stateLists[1]
        else:
            return print("Invalid State")
    else:
        return print("Invalid State")


def max_value_prune(state, alpha, beta):
    key = (tuple(state[0]), state[1], alpha, beta)
    if key in mem:
        return mem[key]
    if not state[0]:
        return [state], 1
    v = float('-inf')
    optimal_path = None
    for s in nextstates(state):
        path, value = min_value_prune(s, alpha, beta)
        if value > v:
            v = value
            optimal_path = [state] + path if path else [state]
        if v >= beta:
            break
        alpha = max(alpha, v)
    mem[key] = (optimal_path, v)
    return optimal_path, v


def min_value_prune(state, alpha, beta):
    key = (tuple(state[0]), state[1], alpha, beta)
    if key in mem:
        return mem[key]
    if not state[0]:
        return [state], -1
    v = float('inf')
    optimal_path = None
    for s in nextstates(state):
        path, value = max_value_prune(s, alpha, beta)
        if value < v:
            v = value
            optimal_path = [state] + path if path else [state]
        if v <= alpha:
            break
        beta = min(beta, v)
    mem[key] = (optimal_path, v)
    return optimal_path, v


def nextstates(state):
    stateList = state[0]
    derived = []
    unique_sub = []
    for i in range(len(stateList)):
        for take in range(1, 4):
            if stateList[i] >= take:
                sub = stateList[:i] + [stateList[i] - take] + stateList[i + 1:]
                sorted_sub = sorted(sub)
                if sorted_sub not in unique_sub:
                    unique_sub.append(sorted_sub)
                    derived.append(sub)
    return [([value for value in sublist if value > 0], (3 - state[1])) for sublist in derived]


# Game, get state
init_state = Nim()
game_begin(init_state)
