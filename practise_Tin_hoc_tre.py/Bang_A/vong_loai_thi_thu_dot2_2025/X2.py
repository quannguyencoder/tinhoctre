n = int(input())

look_up4 = [1, 3, 2, 6]
look_up = [4, 12, 8, 24, 16, 48, 32, 96, 64, 92, 28, 84, 56, 68, 12, 36, 24, 72, 48, 44, 96, 88, 92, 76, 84, 52, 68, 4, 36, 8, 72, 16, 44, 32, 88, 64, 76, 28, 52, 56]

result = sum(look_up4)
if n <= 4:
    print(sum(look_up4[:n]))
else:
    num_cycle = (n - 4) // 40
    sum_cycle = sum(look_up) * num_cycle

    remain_nums = (n - 4) % 40
    sum_remain = sum(look_up[:remain_nums])

    print(result + sum_cycle + sum_remain)




# for index in range(n):
#     if index % 2 == 0:
#         result += (2 ** (index // 2)) % 100
#     else:
#         result += (3 * (2 ** (index // 2))) % 100