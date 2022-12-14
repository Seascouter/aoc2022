contents = []
pairs = []
with open("input.txt") as f:
    for line in f:
        contents.append(line.strip())
        
def part1():
    sum = 0
    for line in contents:
        one, two = line.split(',')
        s1, e1 = one.split('-')
        s2, e2 = two.split('-')
        s1, e1, s2, e2 = [int(x) for x in [s1, e1, s2, e2]]
        print(s1, e1, s2, e2)
        if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
            sum += 1
    return sum
        

def part2():
    sum = 0
    for line in contents:
        one, two = line.split(',')
        s1, e1 = one.split('-')
        s2, e2 = two.split('-')
        s1, e1, s2, e2 = [int(x) for x in [s1, e1, s2, e2]]
        print(s1, e1, s2, e2)
        one = [i for i in range(s1, e1+1)]
        two = [j for j in range(s2, e2+1)]
        for item in one:
            if item in two:
                sum += 1
                break

    return sum


p1 = part1()
p2 = part2()

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")


