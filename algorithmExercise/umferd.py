# https://open.kattis.com/problems/umferd

m = int(input())
n = int(input())
cnt = 0

for i in range(n):
    for j in list(input()):
        if j == ".":
            cnt += 1

print(cnt/(n*m))


# Advanced:
# m, n = int(input()), int(input())
# cnt = sum(row.count('.') for i in range(n) for row in list(input()))
# print(cnt / (n * m))
