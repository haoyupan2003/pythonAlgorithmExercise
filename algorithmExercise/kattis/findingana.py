# https://open.kattis.com/problems/twosum

array = list(input())
index = array.index('a') if 'a' in array else len(array)
print("".join(array[index:]))
