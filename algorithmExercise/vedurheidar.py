# https://open.kattis.com/problems/vedurheidar

w = int(input())
n = int(input())

for _ in range(n):
    line = input().split()
    name = line[0]
    limit = int(line[1])

    if w > limit:
        print(f"{name} lokud")
    else:
        print(f"{name} opin")
