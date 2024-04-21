LYRICS = {
    0: "no green bottles",
    1: "One green bottle",
    2: "Two green bottles",
    3: "Three green bottles",
    4: "Four green bottles",
    5: "Five green bottles",
    6: "Six green bottles",
    7: "Seven green bottles",
    8: "Eight green bottles",
    9: "Nine green bottles",
    10: "Ten green bottles"
}

def recite(start, take=1):
    return_vers = []

    for i in range(take):
        for y in range(2):
            return_vers.append(f"{LYRICS[start - i]} hanging on the wall,")

        return_vers.append(f"And if one green bottle should accidentally fall,")
        return_vers.append(f"There'll be {(LYRICS[start - (i + 1)]).lower()} hanging on the wall.")

        if i + 1 < take: return_vers.append("")
    return return_vers
