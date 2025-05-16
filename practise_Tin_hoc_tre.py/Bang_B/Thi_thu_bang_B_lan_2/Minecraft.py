nums = list(map(int, input().split()))
n, block = nums[0], nums[1]
wall = list(map(int, input().split()))
equal = 0
item = wall[0]
for index in range (1, len(wall)):
    if item == index:
        equal += 1
    item = index
if equal == len(wall):
    print(wall[0] + (block // n)) 