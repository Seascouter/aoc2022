contents = []
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

with open("input.txt") as f:
    for line in f:
        contents.append(line.strip())

def part1():
    global contents, upper, lower
    sum = 0
    for content in contents:
        kSize = len(content)
        pocket_1 = content[:kSize//2]
        pocket_2 = content[kSize//2:kSize]
        for item in pocket_1:
            if item in pocket_2:
                if item.isupper():
                    sum += ord(item) - 38
                else:
                    sum += ord(item) - 96
                break
    return sum

def part2():
    global contents
    sum = 0
    groups = []
    temp = []
    for item in contents:
        temp.append(item)
        if len(temp) == 3:
            groups.append(temp)
            temp = []
    for group in groups:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                if item.isupper():
                    sum += ord(item) - 38
                else:
                    sum += ord(item) - 96
                break
    return sum


        
p1 = part1()
p2 = part2()

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
