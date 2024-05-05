import time

def test_timing(state):
    # Start a timer
    start = time.time()
    # Call minimax function
    value = minimax_prune(state)
    end = time.time()
    # calculate and return
    duration = end - start
    # print('Time taken:', duration)
    return duration, value

mem = {}

def minimax_prune(state):
    if state[0]:
        if state[1] == 1:
            return str(max_value_prune(state, float('-inf'), float('inf')))
        elif state[1] == 2:
            return str(min_value_prune(state, float('-inf'), float('inf')))
        else:
            return str(([], 0))
    else:
        return str(([], 0))


def max_value_prune(state, alpha, beta):
    state = (state[0], 1)
    # Convert state to a hashable key for memoization
    key = (tuple(state[0]), state[1], alpha, beta)
    if key in mem:
        return mem[key]

    if not state[0]:  # Base case
        return [state], 1

    v = float('-inf')
    optimal_path = None
    for s in successor(state):

        path, value = min_value_prune(s, alpha, beta)
        if value > v:
            v = value
            optimal_path = [state] + path if path else [state]
        if v >= beta:  # Alpha-Beta Pruning
            break
        alpha = max(alpha, v)

    # Store the result in mem before returning
    mem[key] = (optimal_path, v)
    return optimal_path, v


def min_value_prune(state, alpha, beta):
    state = (state[0], 2)
    # Convert state to a hashable key for memoization
    key = (tuple(state[0]), state[1], alpha, beta)
    if key in mem:
        return mem[key]

    if not state[0]:  # Base case
        return [state], -1

    v = float('inf')
    optimal_path = None
    for s in successor(state):
        path, value = max_value_prune(s, alpha, beta)
        if value < v:
            v = value
            optimal_path = [state] + path if path else [state]
        if v <= alpha:  # Alpha-Beta Pruning
            break
        beta = min(beta, v)

    # Store the result in mem before returning
    mem[key] = (optimal_path, v)
    return optimal_path, v





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

if __name__ == "__main__":
    print(test_timing(([8, 8], 2))) #1
    print(test_timing(([6, 4, 2, 3], 1))) #1
    print(test_timing(([5, 5, 5], 1))) #-1

    print(test_timing(([8, 8, 8], 1))) #1
    print(test_timing(([20, 20], 1))) #1
    print(test_timing(([10, 10, 10], 2))) #-1
    print(test_timing(([6, 4, 2, 3, 5, 5, 5], 1))) #1
