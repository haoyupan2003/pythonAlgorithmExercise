# https://open.kattis.com/problems/spritt

n, m = map(int, input().split())

total_needed = 0

for _ in range(n):
    need = int(input())
    total_needed += need

if total_needed <= m:
    print("Jebb")
else:
    print("Neibb")
