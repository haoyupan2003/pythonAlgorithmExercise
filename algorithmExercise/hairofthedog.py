# https://open.kattis.com/problems/hairofthedog

cnt = 0
arr = []
n = int(input())

for i in range(n):
    arr.append(input())

for i in range(n):
    if arr[i] == "drunk" and arr[i+1] == "sober":
        cnt += 1

print(cnt)
