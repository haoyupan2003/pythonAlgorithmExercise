# https://open.kattis.com/problems/pobudget

n = int(input())

total = 0

for _ in range(n):
    description = input()
    amount = int(input())
    total += amount

if total > 0:
    print("Usch, vinst")
elif total == 0:
    print("Lagom")
else:
    print("Nekad")
