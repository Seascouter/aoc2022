contents = []
currentElf = []
currentTotal = 0
elves = []

with open("input.txt") as f:
    for line in f:
        contents.append(line.strip())

def part1():
    global contents, currentElf, currentTotal, elves
    for c in contents:
        if c.isnumeric():
            currentElf.append(int(c))
        else:
            for cal in currentElf:
                currentTotal += cal
            elves.append(currentTotal)
            currentElf = []
            currentTotal = 0
    elves.sort()
    return elves[-1]
                
def part2():
    return elves[-1] + elves[-2] + elves[-3]

p1 = part1()
p2 = part2()

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
