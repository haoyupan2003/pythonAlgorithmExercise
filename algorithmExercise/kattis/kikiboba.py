# https://open.kattis.com/problems/kikiboba

b_cnt = 0
k_cnt = 0


for i in input():
    if i == "b":
        b_cnt += 1
    elif i == "k":
        k_cnt += 1

print("boba" if b_cnt > k_cnt else "kiki" if k_cnt >
      b_cnt else "boki" if b_cnt == k_cnt and b_cnt != 0 else "none")
