# Part 1
def collatz(n):
    n = int(round(n))
    if n < 1 or n > 100000:
        return
    arr = [n]
    while n != 1:
        if n % 2 == 0:
            n = (n // 2)
            arr.append(n)
        else:
            n = ((n * 3) + 1)
            arr.append(n)
    return len(arr)


# Part 2
def biggest_seq(end):
    end = int(round(end))
    if end < 1 or end > 100000:
        return None, None
    seqLen = 0
    seqNum = 0
    for i in range(1, end + 1):
        len1 = collatz(i)
        if len1 > seqLen:
            seqNum = i
            seqLen = len1
    return seqNum, seqLen


# Part 3
def has_aaa(s):
    string = str(s)
    if "aaa" in string.lower():
        return True
    return False


# Part 4
def make_bunch(high, low, green, budget):
    high = int(round(high))
    low = int(round(low))
    green = int(round(green))

    if green < 4 or high < 0 or low < 0 or budget < 2:
        return []

    highCount = 0
    lowCount = 0
    greenCount = 4
    green -= 4
    budget -= 2

    while budget > 0:
        if budget >= 4 and highCount < 4 and high > 0:
            highCount += 1
            high -= 1
            budget -= 4
        elif budget >= 2 and low > 0:
            lowCount += 1
            low -= 1
            budget -= 2
        elif budget >= 0.5 and green > 0:
            greenCount += 1
            green -= 1
            budget -= 0.5
        else:
            return []

    arr = [highCount, lowCount, greenCount]
    return arr


# FIX THIS (it works but need touching up)

if __name__ == "__main__":
    print(make_bunch(4, 1, 6, 23))
    print(make_bunch(4, 8, 10, 15))
    print(make_bunch(3, 8, 10, 19))