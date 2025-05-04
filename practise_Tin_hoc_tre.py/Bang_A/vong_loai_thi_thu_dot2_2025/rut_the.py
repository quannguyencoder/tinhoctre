n = int(input()) # 6
k = int(input()) # 15

sum_n = n * (n + 1) // 2
num_turns = (k // (n + 1)) * 2
next_num = num_turns // 2 + 1

if sum_n <= k:
    print(0)
else: # sum_n < k
    if (num_turns // 2) * (n + 1) < k:
        print("num_turns:", num_turns)
        print("next_num:", next_num)
        if (num_turns // 2) * (n + 1) + next_num > k:
            print(num_turns + 1)
        else:
            print(num_turns + 2)