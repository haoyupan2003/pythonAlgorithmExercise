# https://open.kattis.com/problems/skak

cnt = 0
p = list(map(int, input().split()))
g = list(map(int, input().split()))

if p[0] != g[0]:
    cnt += 1
if p[1] != g[1]:
    cnt += 1

print(cnt)
