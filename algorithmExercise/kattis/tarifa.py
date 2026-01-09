# https://open.kattis.com/problems/tarifa

X = int(input())
N = int(input())
total_used = 0
for _ in range(N):
    used = int(input())
    total_used += used

available = X * (N + 1) - total_used
print(available)
