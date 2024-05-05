import time


def test_timing(state):
    start = time.time()
    value = minimax_prune(state)
    end = time.time()
    duration = end - start
    return duration, value


def minimax_prune(state):
    if state[0]:
        if state[1] == 1:
            return str(max_value_prune(state, float('-inf'), float('inf')))
        elif state[1] == 2:
            return str(min_value_prune(state, float('-inf'), float('inf')))
    else:
        return str(0)


mem = {}


def max_value_prune(state, alpha, beta):
    key = (tuple(state[0]), 1, alpha, beta)
    if key in mem:
        return mem[key]
    if not state[0]:
        return 1
    v = float('-inf')
    for s in successor(state):
        v = max(v, min_value_prune(s, alpha, beta))
        if v >= beta:
            break
        alpha = max(alpha, v)
    mem[key] = v
    return v


def min_value_prune(state, alpha, beta):
    key = (tuple(state[0]), 2, alpha, beta)
    if key in mem:
        return mem[key]
    if not state[0]:
        return -1
    v = float('inf')
    for s in successor(state):
        v = min(v, max_value_prune(s, alpha, beta))
        if v <= alpha:
            break
        beta = min(beta, v)
    mem[key] = v
    return v


def successor(state):
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

    return [([value for value in sublist if value > 0], state[1]) for sublist in derived]


'''
this is a much more efficient solution 

def successor(state):
    stateList = state[0]
    derived = set()  # Use a set to store unique state representations

    for i, value in enumerate(stateList):
        for take in range(1, min(4, value + 1)):  # Ensure valid takes
            # Generate the new state
            new_state = stateList[:i] + [value - take] + stateList[i + 1:]
            # Filter out non-positive values and create a sorted tuple for uniqueness
            new_state_filtered_sorted = tuple(sorted(v for v in new_state if v > 0))
            # Add the unique, filtered, and sorted state representation to the set
            derived.add(new_state_filtered_sorted)

    # Convert the unique states back into the desired format
    return [(list(state), player) for state in derived]
'''

if __name__ == "__main__":
    print(test_timing(([8, 8], 2)))  # -1
    print(test_timing(([6, 4, 2, 3], 1)))  # 1
    print(test_timing(([5, 5, 5], 1)))  # -1

    print(test_timing(([8, 8, 8], 1)))  # 1
    print(test_timing(([20, 20], 1)))  # 1
    print(test_timing(([10, 10, 10], 2)))  # -1
    print(test_timing(([6, 4, 2, 3, 5, 5, 5], 1)))  # 1
