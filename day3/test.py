with open('input.txt') as file:
    lines = file.read().splitlines()
a = [chr(i) for i in range(97, 97+26)]
a.extend([chr(i) for i in range(65, 65+26)])
ans = 0
print(lines[:2])
for line in lines:
    n = len(line)
    s, t = line[:n//2], line[n//2:]
    u, v = set(s), set(t)
    c = u.intersection(v).pop()
    p = a.index(c) + 1
    ans += p
print(ans)
