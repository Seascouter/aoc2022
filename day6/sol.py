contents = []

with open("input.txt") as f:
    for line in f:
        contents.append(line.strip())

string = contents[0]

def part1():
    global string
    for i in range(len(string)):
        chars = []
        for x in range(4):
            if string[i+x] in chars:
                break
            else:
                chars.append(string[i+x])
        print(chars, len(chars))
        if len(chars) == 4:
            return i + 4

def part2():
    global string
    for i in range(len(string)):
        chars = []
        for x in range(14):
            if string[i+x] in chars:
                break
            else:
                chars.append(string[i+x])
        print(chars, len(chars))
        if len(chars) == 14:
            return i + 14
    

p1 = part1()
p2 = part2()

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
