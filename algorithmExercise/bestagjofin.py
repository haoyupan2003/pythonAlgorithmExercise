# https://open.kattis.com/problems/bestagjofin

dict = {}

for i in range(int(input())):
    a, b = input().split()
    dict[a] = int(b)

sorted_dict = sorted(dict.items(), key=lambda x: x[1])

print(sorted_dict[-1][0])
