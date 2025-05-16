nums = list(map(int, input().split()))
a = nums[0]
rank = 1
for index in range(1, len(nums)):
    if nums[index] > a:
        rank += 1
print(rank)
