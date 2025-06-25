# https://open.kattis.com/problems/pet

max_points = 0
winner = 0

for i in range(1, 6):
    grades = list(map(int, input().split()))
    total = sum(grades)
    if total > max_points:
        max_points = total
        winner = i

print(f"{winner} {max_points}")
