# https://open.kattis.com/problems/oddecho

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for i in range(n):
    if i % 2 == 0:
        print(arr[i])
