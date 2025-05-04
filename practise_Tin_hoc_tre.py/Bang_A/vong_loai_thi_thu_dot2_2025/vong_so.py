n = list(input())
k = int(input())
nums = list(map(int, n))
for index in range(len(nums)):
    nums[index] = (nums[index] + k) % 10
result = list(map(str, nums))
print(''.join(result))