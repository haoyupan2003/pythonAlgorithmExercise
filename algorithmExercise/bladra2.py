# https://open.kattis.com/problems/bladra2

array = input().split(" ")

v = float(array[0])
a = float(array[1])
t = float(array[2])

print(f"{(v*t)+((a*(t**2))/2):.9f}")
