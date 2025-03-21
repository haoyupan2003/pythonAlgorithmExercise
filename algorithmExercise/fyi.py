# https://open.kattis.com/problems/fyi

telephoneNum = list(input())
if int(telephoneNum[0]) == 5 and int(telephoneNum[1]) == 5 and int(telephoneNum[2]) == 5:
    print(1)
else:
    print(0)


# Advanced:
# print(1 if input().startswith("555") else 0)
