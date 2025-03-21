# https://open.kattis.com/problems/dagatal
x = int(input())

print(28 if x == 2 else 30 if x in (4, 6, 9, 11) else 31)
