a = int(input())
n = int(input())
k_new = a // 2
k = a // 2
nums = []
index = 1
sum20 = 0
result = 0
remain = n % 20
sum_remain = 0
while index <= 20:
    num = a % 10
    if index % 2 != 0:
        if index <= remain:
            sum_remain += num

        sum20 += num
        a += k
        #-----------
    else:
        if index <= remain:
            sum_remain += num

        sum20 += num
        k_new += k

    index += 1

n_sum20 = n // 20
result += n_sum20 * sum20 + sum_remain
print(result)
# if n % 20 == 0:
#     print(result)
# else:
#     print(result + sum_remain)    