def next_states(s):
    s = str(s).upper().replace(" ", "")
    derived = []
    if s == "":
        return derived
    if s[-1] == "I":
        n = s + "U"
        if n not in derived:
            derived.append(n)
    if s[0] == "M":
        n = s[0] + s[1:] + s[1:]
        if n not in derived:
            derived.append(n)
    i = 0
    while "UU" in s[i:]:
        i2 = s.find("UU", i)
        n = s[:i2] + s[i2 + 2:]
        if n not in derived:
            derived.append(n)
        i = i2 + 1
    i = 0
    while "III" in s[i:]:
        i2 = s.find("III", i)
        n = s[:i2] + "U" + s[i2 + 3:]
        if n not in derived:
            derived.append(n)
        i = i2 + 1
    return derived


def extend_path(s):
    if not isinstance(s, list) or s == []:
        return []
    outList = []
    nextStates = next_states(s[-1])
    for elements in nextStates:
        path = s.copy()
        path.append(elements)
        outList.append(path)
    return outList


def breadth_first_search(goalString):
    goalState = str(goalString).upper().replace(" ", "")
    extendCount = 0
    agendaMaxLen = 0
    agenda = [["MI"]]
    while True:
        if extendCount > 4999 or goalState == "":
            return [0, 0, 0]
        if len(agenda) > agendaMaxLen:
            agendaMaxLen = len(agenda)
        currentPath = agenda[0]
        agenda.pop(0)
        if currentPath[-1] == goalState:
            return currentPath, extendCount, agendaMaxLen
        else:
            s = [currentPath[0], currentPath[-1]]
            lastElements = [sublist[-1] for sublist in extend_path(s)]
            newAgenda = [currentPath + [lElement] for lElement in lastElements]
            agenda.extend(newAgenda)
            extendCount += 1


depthextendCount = 0
depthMaxAgendaLen = 0


def depthlimited_dfs(goalString, limit):
    goalState = str(goalString).upper().replace(" ", "")
    limit = int(limit)
    global depthextendCount
    global depthMaxAgendaLen
    extendCount = 0
    agendaMaxLen = 0
    agenda = [["MI"]]
    while True:
        if extendCount > 4999 or goalState == "" or agenda == []:
            return [0, 0, 0]
        if len(agenda) > agendaMaxLen:
            agendaMaxLen = len(agenda)
            if agendaMaxLen > depthMaxAgendaLen:
                depthMaxAgendaLen = agendaMaxLen
        currentPath = agenda.pop(0)
        if len(currentPath) <= limit:
            state = [currentPath[0], currentPath[-1]]
            lastElements = [sublist[-1] for sublist in extend_path(state)]
            extendCount += 1
            depthextendCount += 1
            newAgenda = [currentPath + [lElement] for lElement in lastElements]
            for path in reversed(newAgenda):
                agenda.insert(0, path)
        if currentPath[-1] == goalState:
            return currentPath, extendCount, agendaMaxLen


def dfs_iter(goalstring):
    goalString = str(goalstring).upper().replace(" ", "")
    limit = 2
    global depthextendCount
    global depthMaxAgendaLen
    depthMaxAgendaLen = 0
    depthextendCount = 0
    while True:
        if depthextendCount > 4999:
            return [0, 0, 0]
        alg = depthlimited_dfs(goalString, limit)
        limit += 1
        if alg != [0, 0, 0]:
            out = alg[0], (depthextendCount + 1), depthMaxAgendaLen
            return out


if __name__ == "__main__":
    print(breadth_first_search("MIUUIUUIIUU"))
    print(depthlimited_dfs("MIUUIUUIIUU", 4))
    print(depthlimited_dfs("MIIII", 3))
    print(dfs_iter("MUIU"))
    print(dfs_iter("MUIUII"))

