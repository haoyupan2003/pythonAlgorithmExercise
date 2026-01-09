# https://open.kattis.com/problems/sorttwonumbers

a, b = input().split(" ")

print(a+" "+b if int(a) < int(b) else b+" "+a)
