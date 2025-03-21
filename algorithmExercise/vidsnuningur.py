# https://open.kattis.com/problems/vidsnuningur

a = input()
result = ""

for i in range(len(a)):
    result += a[-i-1]

print(result)

# Advanced:
# print(input()[::-1])
