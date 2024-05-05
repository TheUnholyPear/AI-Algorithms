def minimax_value(state):
    if state[0]:
        if state[1] == 1:
            return max_func(state)
        elif state[1] == 2:
            return min_func(state)
        else:
            return "Invalid player"
    else:
        return "Invalid state"


def max_func(state):
    state = (state[0], 1)
    if not state[0]:
        return [state], 1
    v = float('-inf')
    optimal_path = None
    for s in successor(state):
        path, value = min_func(s)
        if value > v:
            v = value
            optimal_path = [state] + path if path else [state]
    return optimal_path, v


def min_func(state):
    state = (state[0], 2)
    if not state[0]:
        return [state], -1
    v = float('inf')
    optimal_path = None
    for s in successor(state):
        path, value = max_func(s)
        if value < v:
            v = value
            optimal_path = [state] + path if path else [state]
    return optimal_path, v


def successor(state):
    stateList = state[0]
    derived = []
    for i in range(len(stateList)):
        for take in range(1, 4):
            if stateList[i] >= take:
                sub = stateList[:i] + [stateList[i] - take] + stateList[i + 1:]
                derived.append(sub)
    derived = [([value for value in sublist if value > 0], state[1]) for sublist in derived]
    return derived


if __name__ == "__main__":
    print(minimax_value(([4], 1)))  # ([([4], 1), ([1], 2), ([], 1)], 1)
    print(minimax_value(([2, 3], 1)))  # ([([2, 3], 1)([2, 2], 2)([1, 2], 1)([1], 2)([], 1)], 1)
    print(minimax_value(([5, 5, 5],
                         1)))  # ([([5, 5, 5], 1)([4, 5, 5], 2)([1, 5, 5], 1)([5, 5], 2)([4, 5], 1)([3, 5], 2)([5], 1)([4], 2)([1], 1)([], 2)], -1)
    print(minimax_value(([1, 2], 2)))  # ([([1, 2], 2)([1], 1)([], 2)],-1)
