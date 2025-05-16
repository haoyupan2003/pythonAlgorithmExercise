# https://open.kattis.com/problems/oddecho

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
    input()

for i in range(len(arr)):
    print(arr[i])
