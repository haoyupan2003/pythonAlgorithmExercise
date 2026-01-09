# https://open.kattis.com/problems/hakkari

R, C = map(int, input().split())
mines = []

for r in range(1, R + 1):
    row = input().strip()
    for c in range(1, C + 1):
        if row[c - 1] == '*':
            mines.append((r, c))

print(len(mines))
for r, c in mines:
    print(r, c)
