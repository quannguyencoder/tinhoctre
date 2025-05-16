n, k = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list = list(map(int, input().split()))
result = 0
cur_len = 0
for index in range(n-1):
    cur_num = a_list[index]
    cur_sum = b_list[index]
    cur_len = 1
    for next_index in range(index + 1, n):
        if (cur_num % a_list[next_index]) == 0 and (cur_sum + b_list[next_index]) <= k:
            cur_len += 1
            cur_sum += b_list[next_index]
            cur_num = a_list[next_index]
        elif cur_len > 1:
            result = max(result, cur_len)
            break


        # if cur_len == 1:
        #     cur_len = 0
    
            
result = max(result, cur_len)

print(result)