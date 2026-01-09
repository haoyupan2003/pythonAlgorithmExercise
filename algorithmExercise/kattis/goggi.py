# https://open.kattis.com/problems/goggi

line = input()

a_str, _, b_str = line.split()

a = int(a_str)
b = int(b_str)

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("Goggi svangur!")
