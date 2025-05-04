n = int(input())
nums = input()
nums = list(map(int, nums.split()))
number = []
result = 0
remain = 0
if len(nums) == 2:
    if (nums[0] > nums[1] and nums[0] % nums[1] == 0) or (nums[1] > nums[0] and nums[1] % nums[0] == 0) :
        result += 1
        print(result)
    else:
        result += 2
        print(result)
else:
    for index in range (1, n-1):
        for index in range (index + 1, n):
            if (nums[index] > nums[index - 1] and nums[index] % nums[index - 1]  != 0) or (nums[index - 1] > nums[index] and nums[index - 1] % nums[index] != 0):
                result += 1
        number.append(result)
        result = 0
    if max(number) == 1:
        print(max(number) + 1)
    else:
        print(max(number))