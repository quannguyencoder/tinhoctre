n = int(input())
nums_str = input()
a_str = nums_str.split(' ')
nums_int = list((map(int, a_str)))
num0 = 0
num1 = 0
num2 = 0
result = 0
mean = n // 3

# for index in range(len(nums_int) - 1):
#     if nums_int[index] % 3 == 0:
#         num0 += 1
#     elif nums_int[index] % 3 == 1:
#         num1 += 1
#     elif nums_int[index] % 3 == 2:
#         num2 += 1

for num in nums_int:
    if num % 3 == 0:
        num0 += 1
    elif num % 3 == 1:
        num1 += 1
    elif num % 3 == 2:
        num2 += 1

if num0 > mean:
    result += num0 - mean

if num1 > mean:
    result += num1 - mean

if num2 > mean:
    result += num2 - mean
print (result)