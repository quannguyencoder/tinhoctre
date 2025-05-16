n, k = list(map(int, input().split()))
a_list = list(map(int, input().split()))
a_list.sort(reverse=False)
max_len = 0
len_list = 1
for index in range(n - 1):
    if abs(a_list[index] - a_list[index + 1]) <= k:
        len_list += 1
    else:
        if len_list > max_len:
            max_len = len_list
        len_list = 0
if len_list > max_len:
    max_len = len_list
print(max_len)