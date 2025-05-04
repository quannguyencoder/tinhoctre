k = int(input())
n = int(input())
nums = n // k
result = (nums * (nums + 1) // 2 ) * k
result += (n % k) * (nums + 1)
print(result % 100)