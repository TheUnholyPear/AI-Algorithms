import time


def test_timing(state):
    # Start a timer
    start = time.time()
    # Call minimax function
    value = minimax_value(state)
    end = time.time()
    # calculate and return
    duration = end - start
    # print('Time taken:', duration)
    return duration, value


def minimax_value(state):
    if state[0]:
        if state[1] == 1:
            return str(max_func(state))
        elif state[1] == 2:
            return str(min_func(state))
        else:
            return str(0)
    else:
        return str(0)


def max_func(state):
    state = (state[0], 1)
    if not state[0]:
        return 1
    v = float('-inf')
    for s in successor(state):
        v = max(v, min_func(s))
    return v


def min_func(state):
    state = (state[0], 2)
    if not state[0]:
        return -1
    v = float('inf')
    for s in successor(state):
        v = min(v, max_func(s))
    return v


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
    # print(minimax_value(([5], 1)))
    # print(minimax_value(([4], 1)))
    # print(minimax_value(([2, 3], 1)))
    # print(minimax_value(([1, 2], 2)))
    # print(minimax_value(([5, 5, 5], 1)))

    # print((test_timing(([5, 5], 2))))
    # print((test_timing(([4], 1))))
    # print(test_timing(([2, 3], 1)))
    # print(test_timing(([9, 9], 1)))
    # print((test_timing(([5, 5, 5], 1))))

    #print(minimax_value(([4], 1)))
    #print(minimax_value(([2, 3], 1)))
    print(minimax_value(([5, 5, 5], 1)))
    #print(minimax_value(([1, 2], 2)))
