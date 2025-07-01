# https://open.kattis.com/problems/knotknowledge

n = int(input())
needed = list(map(int, input().split()))
learned = list(map(int, input().split()))

missing = sum(needed) - sum(learned)
print(missing)
