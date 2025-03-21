# https://open.kattis.com/problems/blandadbest

kjuklingur_cnt = 0
nautakjot_cnt = 0


for i in range(int(input())):
    if input() == "kjuklingur":
        kjuklingur_cnt += 1
    else:
        nautakjot_cnt += 1

if kjuklingur_cnt == 0:
    print("nautakjot")
elif nautakjot_cnt == 0:
    print("kjuklingur")
else:
    print("blandad best")


# Advanced:
# print("blandad best" if (x := [input() for i in range(int(input()))]).count("kjuklingur") > 0 and x.count(
#     "nautakjot") > 0 else ("kjuklingur" if x.count("nautakjot") == 0 else "nautakjot"))
