# https://open.kattis.com/problems/wakeupcall
n, m = map(int, input().split())
s1c = s2c = 0
s1 = input().split()
s2 = input().split()

for i in range(n):
    s1c += int(s1[i])

for j in range(m):
    s2c += int(s2[j])

if s1c > s2c:
    print("Button 1")
elif s1c < s2c:
    print("Button 2")
else:
    print("Oh no")
