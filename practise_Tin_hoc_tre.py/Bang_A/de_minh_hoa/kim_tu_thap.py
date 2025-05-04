n = int(input())
result = n * (n + 1) * (2 * n + 1) // 6
if n <= 1000:
    print(result)
else:
    print(result % 1000)
