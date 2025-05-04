# tach chuoi input co dinh dang: n m => vao 1 list
n_m = input()
n_m_list = n_m.split(' ')
# neu list co 2 phan tu, co the gan truc tiep: n, m = n_m_list
n, m = int(n_m_list[0]), int(n_m_list[1])

day_n = input()
day_n_ls = day_n.split(' ')
day_n_int = list(map(int, day_n_ls))

full_nums = [x for x in range(1, m + 1)]
nums = list(set(full_nums) - set(day_n_int))

if len(nums) > 0:
    result = 1
    for item in nums:
        result *= item
    print(result % (10 ** 9 + 7))
else:
    print(0)