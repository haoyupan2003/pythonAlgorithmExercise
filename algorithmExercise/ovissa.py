# https://open.kattis.com/problems/ovissa

array = list(input())
cnt = 0
for i in array:
    if i == "u":
        cnt += 1
print(cnt)
