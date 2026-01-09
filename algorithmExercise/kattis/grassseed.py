# https://open.kattis.com/problems/grassseed

cost_per_sqm = float(input())
n = int(input())
total_cost = 0.0
for _ in range(n):
    w, l = map(float, input().split())
    total_cost += w * l * cost_per_sqm
print(f"{total_cost:.7f}")
