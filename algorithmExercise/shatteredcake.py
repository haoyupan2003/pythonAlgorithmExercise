# https://open.kattis.com/problems/shatteredcake

W = int(input())
N = int(input())
total_area = 0
for _ in range(N):
    w, l = map(int, input().split())
    total_area += w * l
print(total_area // W)
