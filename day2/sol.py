contents = []

scores = {"A":1,
          "B":2,
          "C":3}

with open("input.txt") as f:
    for line in f:
        contents.append(line.strip())

def scoreLine(line):
    global scores
    oppMove = line[0]
    youMove = line[2]
    swap = {"X":"A",
            "Y":"B",
            "Z":"C"}
    youMove = swap[youMove]
    # tie
    if oppMove == youMove:
        return 3 + scores[youMove]
    # rock vs paper
    if youMove == "A" and oppMove == "B":
        return scores[youMove]
    # rock vs scissors
    if youMove == "A" and oppMove == "C":
        return 6 + scores[youMove]
    # paper vs scissors
    if youMove == "B" and oppMove == "C":
        return scores[youMove]
    # paper vs rock
    if youMove == "B" and oppMove == "A":
        return 6 + scores[youMove]
    # scissors vs rock
    if youMove == "C" and oppMove == "A":
        return scores[youMove]
    # scissors vs paper
    if youMove == "C" and oppMove == "B":
        return 6 + scores[youMove]
    
def playLine(line):
    global scores
    oppMove = line[0]
    result = line[2]

    # tie
    if result == "Y":
        return 3 + scores[oppMove]
    # lose
    if result == "X":
        # to rock
        if oppMove == "A":
            return scores["C"]
        # to paper
        if oppMove == "B":
            return scores["A"]
        # to scissors
        if oppMove == "C":
            return scores["B"]
    # win
    if result == "Z":
        # against rock
        if oppMove == "A":
            return 6 + scores["B"]
        # against paper
        if oppMove == "B":
            return 6 + scores["C"]
        # against scissors
        if oppMove == "C":
            return 6 + scores["A"]
            

    
    
def part1():
    score = 0
    for content in contents:
        score += scoreLine(content)
    return score

def part2():
    score = 0
    for content in contents:
        score += playLine(content)
    return score

p1 = part1()
p2 = part2()

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")



