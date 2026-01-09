# https://open.kattis.com/problems/jumbojavelin

n = int(input())
total = 0

for _ in range(n):
    length = int(input())
    total += length

total -= (n - 1)

print(total)
