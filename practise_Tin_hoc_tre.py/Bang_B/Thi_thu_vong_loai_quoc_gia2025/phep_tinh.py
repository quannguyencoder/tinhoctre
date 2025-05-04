T = int(input())
nums_input = []
for _ in range(T):
    abc = input()
    nums_input.append(list(map(int, abc.split(' '))))

for nums in nums_input:
    a, b, c = nums
    if a + b == c:
        print("+")
    elif a - b == c:
        print("-")
    elif a * b == c:
        print("*")
    elif a // b == c:
        print("/")
    else:
        print("None")