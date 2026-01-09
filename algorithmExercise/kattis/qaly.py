# https://open.kattis.com/problems/qaly

n = int(input())
total_qaly = 0.0

for _ in range(n):
    q, y = map(float, input().split())
    total_qaly += q * y

print(f"{total_qaly:.3f}")
