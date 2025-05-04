nums = []
num1 = 0
num2 = 0
for index in range(5):
    nums.append(int(input()))
for item in nums:
    if item == 1:
        num1 += 1
    else:
        num2 += 1
if num1 > num2:
    print("1")
else:
    print("2")
# print("num1:",num1)
# print("num2:",num2)