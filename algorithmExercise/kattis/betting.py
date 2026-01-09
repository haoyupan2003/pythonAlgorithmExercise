# https://open.kattis.com/problems/betting

p = int(input())
print(f"{100 / p:.10f}")
print(f"{100 / (100 - p):.10f}")
