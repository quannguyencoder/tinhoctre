k = int(input())
if k % 7 == 0:
    print(8)
else:
    result = (8 + k % 7) % 7
    print(result)