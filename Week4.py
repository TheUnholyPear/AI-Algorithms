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


def breadth_first_dictionarysearch(goalString):
    goalState = str(goalString).upper().replace(" ", "")
    extendCount = 0
    agendaMaxLen = 0
    agenda = ["MI"]
    hashAgenda = {"MI": ["start", "N"]}
    while True:
        if extendCount > 4999 or goalState == "" or agenda == []:
            return [0, 0, 0]
        if len(agenda) > agendaMaxLen:
            agendaMaxLen = len(agenda)
        currentNode = agenda.pop(0)
        if hashAgenda[currentNode][1] == "N":
            lastElements = [element for element in next_states(currentNode) if element not in hashAgenda.keys()]
            for element in lastElements:
                hashAgenda[element] = [currentNode, "N"]
            agenda.extend(lastElements)
            hashAgenda[currentNode][1] = "Y"
            extendCount += 1
        if currentNode == goalState:
            currentPath = [currentNode]
            while True:
                if currentNode == 'MI':
                    return currentPath, extendCount, agendaMaxLen
                currentPath = [hashAgenda[currentNode][0]] + currentPath
                currentNode = hashAgenda[currentNode][0]


def estimate_steps(current, goal):
    heuristic = 0
    if current != goal:
        totalC = current.count("I") + (current.count("U") * 3)
        totalG = goal.count("I") + (goal.count("U") * 3)
        if totalC > (totalG + 12):
            if totalC > (totalG + 18):
                heuristic = 4
            else:
                heuristic = 3
        elif (goal.count("I") != current.count("I") and goal.count("U") != current.count("U")) and (
                goal.count("I") != (current.count("I") - 3) and goal.count("U") != (
                current.count("U") + 1)) and totalC > (totalG / 2):
            heuristic = 2
        else:
            heuristic = 1
    return current, heuristic


def estimate_steps2(current, goal):
    heuristic = 0
    if current != goal:
        heuristic = 1
    return current, heuristic


def a_star_search(goalString):
    goalState = str(goalString).upper().replace(" ", "")
    extendCount = 0
    agendaMaxLen = 0
    agenda = ["MI"]
    hashAgenda = {"MI": ["start", "N", 0]}
    while True:
        if extendCount > 4999 or goalState == "" or agenda == []:
            return [0, 0, 0]
        if len(agenda) > agendaMaxLen:
            agendaMaxLen = len(agenda)
        currentNode = min(agenda, key=(lambda x: hashAgenda[x][2]))
        agenda.remove(currentNode)
        if hashAgenda[currentNode][1] == "N":
            lastElements = [element for element in next_states(currentNode) if element not in hashAgenda.keys()]
            for element in lastElements:
                hashAgenda[element] = [currentNode, "N",
                                       (hashAgenda[currentNode][2] + estimate_steps(element, goalState)[1])]
            agenda.extend(lastElements)
            hashAgenda[currentNode][1] = "Y"
            extendCount += 1
        if currentNode == goalState:
            currentPath = [currentNode]
            while True:
                if currentNode == 'MI':
                    return currentPath, extendCount, agendaMaxLen
                currentPath = [hashAgenda[currentNode][0]] + currentPath
                currentNode = hashAgenda[currentNode][0]


if __name__ == "__main__":
    #print(breadth_first_dictionarysearch('MUIU'))
    #print(breadth_first_dictionarysearch('MIUUIUUII'))
    #print(a_star_search("MUIU"))
    print(a_star_search("MIUUIUUII"))
    #print(a_star_search("MUUUIIIII"))
