from collections import defaultdict

contents = []

with open("input.txt") as f:
    for line in f:
        contents.append(line.strip())




def part1():
    global contents
    
    filesystem = defaultdict(int)
    path = []
    ans = 0

    for line in contents:
        words = line.split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            sz = int(words[0])
            for i in range(len(path)+1):
                filesystem['/'.join(path[:i])] += sz

    for key, value in filesystem.items():
        if value <= 100000:
            ans += value
    return ans

                

def part2():
    global contents
    
    filesystem = defaultdict(int)
    path = []


    for line in contents:
        words = line.split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            sz = int(words[0])
            for i in range(len(path)+1):
                filesystem['/'.join(path[:i])] += sz

    maxUsed = 70000000 - 30000000
    spaceUsed = filesystem['/']
    amtToDelete = spaceUsed - maxUsed
    smallestDir = 1e9
    for key, value in filesystem.items():
        if value >= amtToDelete:
            smallestDir = min(value, smallestDir)

    return smallestDir

p1 = part1()
p2 = part2()

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
