# https://open.kattis.com/problems/fjoldibokstafa

s = input()
count = sum(1 for c in s if c.isalpha())
print(count)
