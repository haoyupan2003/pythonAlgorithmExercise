# https://open.kattis.com/problems/aleidibio

a = int(input())
b = int(input())
c = int(input())

print(c - a - b)


# Extension:
# What if you need to show correct minutes?

# I.e. for the second example:

# Input:
# 8
# 10
# 1000

# Output:
# 942

# Code:
# a = int(input())
# b = int(input())
# c = int(input())


# n = (a + b) // 60
# k = (a + b) % 60
# hours = (c - 100 * n) // 100
# minutes = (c - 100 * n) % 100

# if minutes < k:
#     minutes = minutes + 60 - k
#     hours -= 1
# else:
#     minutes -= k


# print((hours * 100) + minutes)
