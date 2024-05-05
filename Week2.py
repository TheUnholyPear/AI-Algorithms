# Rule 1: ends I, add a U on end
# Rule 2: starts with M, double what comes after M
# Rule 3: III in a string, replace it with a U
# Rule 4: UU in a string, you can delete it

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



if __name__ == "__main__":
    print(next_states("MI"))
    print(next_states("MIU"))
    print(next_states("MUI"))
    print(next_states("MIIII"))
    print(next_states("MUUII"))
    print(next_states("MUUUI"))
    print(next_states("MIIIMMMMMMMMIII"))
