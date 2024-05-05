import random
import time
import math


def test_timing(state):
    # Start a timer
    start = time.time()
    # Call minimax function
    value = AI_player_rollout(state)
    end = time.time()
    # calculate and return
    duration = end - start
    # print('Time taken:', duration)
    return duration, value


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
    mem.clear()
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

    print("\ngame start ", game_state)
    # while no winner, keep alternating
    while game_state[0] != []:

        # You will need to create your own AI function
        if (game_state[1] == 1):
            print("Your turn")
            game_state = (userturn(game_state)[0], 2)
            # game_state = AI_player_basic(game_state)
        else:
            print("AI's turn:")
            calc_time, game_state = test_timing(game_state)
            print("AI moved to state " + str(game_state[0]) + "\n")
            print("Time taken was " + str(calc_time) + "\n")
        # game_state = AI_player_basic(game_state)
        print("new state is", str(game_state))

    # if final state is 1, 2 wins
    if (game_state[1] == 2):
        print("win for player 2 (AI)")
    else:
        print("You win! (Player)")


# tree triversal
# node expansion
# rollout
# back propigation

# no leaf node, choose child with ucb1

mem = {}


def AI_player_rollout(state):
    mem.clear()
    if state[0]:
        if state[1] == 2:
            root_state = (tuple(state[0]), state[1])
            mem[root_state] = [["start"], 0, 0, True, 0]  # parent, visits, totalValue, expanded?

            for suc in nextstates(state):
                key = (tuple(suc[0]), suc[1])
                mem[key] = [state, 0, 0, False, 0]  # Parent, visits, totalValue, expanded?
            path = Limited_MCTS(state)
            return path[1]

        else:
            return print("Invalid State")
    else:
        return print("Invalid State")


def re_create(state):
    path = [state]
    current_state = state
    while current_state[0]:
        var = float("-inf")
        best_next_state = None
        for next_state in nextstates(current_state):
            key = (tuple(next_state[0]), next_state[1])
            if key in mem:
                if UCB1(next_state, True) > var:
                    var = UCB1(next_state, True)
                    best_next_state = next_state
        if best_next_state:
            path.append(best_next_state)
            current_state = best_next_state
        else:
            break
    return path


def Limited_MCTS(state, count_Iter=5000):
    for i in range(count_Iter):
        MCTS(state)
    return re_create(state)


def backPropagate(state, val):
    while state[0] != "start":
        key = (tuple(state[0]), state[1])
        mem[key][1] += 1
        mem[key][2] += val
        state = mem[key][0]


def node_expansion(state):
    mem[tuple(state[0]), state[1]][3] = True
    for next_state in nextstates(state):
        key = (tuple(next_state[0]), next_state[1])
        mem[key] = [state, 0, 0, False, 0]


def MCTS(state):

    while mem[(tuple(state[0]), state[1])][3]:
        new_state = calChild(state)
        state = new_state
        if not state[0]:
            if state[1] == 2:
                val = 1
            else:
                val = -1
            backPropagate(state, val)
            return

    leaf_state = state

    if mem[(tuple(leaf_state[0]), leaf_state[1])][1] == 0 or not leaf_state[0]:
        # Rollout and backpropagation for unvisited node
        backPropagate(leaf_state, simulate_rollout(leaf_state))
    else:
        # Expand and rollout for visited node
        node_expansion(leaf_state)
        mem[(tuple(leaf_state[0]), leaf_state[1])][3] = True  # Mark as expanded
        if leaf_state[0]:
            leaf_state = calChild(leaf_state)
            result = simulate_rollout(leaf_state)
            backPropagate(leaf_state, result)
    return


def UCB1(state, isBest):
    key = (tuple(state[0]), state[1])
    if mem[key][1] == 0 and not isBest and not isBest:
        return float("inf")

    total_value = mem[key][2]
    visits = mem[key][1]
    parent = mem[key][0]

    if parent == "start" or mem[tuple(parent[0]), parent[1]][1] == 0 and not isBest:
        return float('inf')

    parent_visits = mem[tuple(parent[0]), parent[1]][1]

    if isBest:
        if total_value == 0 or visits == 0:
            mem[key][4] = 0
            return 0
        calc = total_value / visits
        mem[key][4] = calc
        return calc

    avg_value = total_value / visits
    sqrt_log = math.sqrt(math.log(parent_visits) / visits)
    c_factor = 3 * sqrt_log

    calc = avg_value + c_factor
    mem[key][4] = calc
    return calc


def calChild(state):
    children = nextstates(state)
    best_val = float('-inf')
    best_state = None
    for child in children:
        child_key = (tuple(child[0]), child[1])
        if child_key in mem:
            val = UCB1(child, False)
            if val > best_val:
                best_val = val
                best_state = child
    return best_state


def simulate_rollout(state):
    if not state[0]:
        if state[1] == 2:
            return 1
        return -1
    next_state = random.choice(nextstates(state))
    return simulate_rollout(next_state)


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


if __name__ == "__main__":
    # print(test_timing(([20, 20, 20, 20, 20], 2)))
    # print(test_timing(([49, 36, 27, 18, 2], 2)))
    # print(test_timing(([49, 36, 37, 38, 39], 2)))
    # print(test_timing(([21, 22, 23, 25, 26], 2)))
    init_state = Nim()
    game_begin(init_state)
