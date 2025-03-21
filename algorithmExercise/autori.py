# https://open.kattis.com/problems/autori

a = input()

result = list(a)[0]


for i in range(len(a)):
    if list(a)[i] == "-":
        result += list(a)[i+1]

print(result)
