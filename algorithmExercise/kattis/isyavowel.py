# https://open.kattis.com/problems/isyavowel

word = input().strip()
vowels_without_y = {'a', 'e', 'i', 'o', 'u'}
vowels_with_y = {'a', 'e', 'i', 'o', 'u', 'y'}
count_without_y = sum(1 for char in word if char in vowels_without_y)
count_with_y = sum(1 for char in word if char in vowels_with_y)
print(count_without_y, count_with_y)
