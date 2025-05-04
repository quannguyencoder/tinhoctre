n = int(input())
result = 0 #tong so tien mua
if n // 10 != 0:
    result += (n // 10) * 17
    n = n % 10
    
if n // 5 != 0:
    result += (n // 5) * 9
    n = n % 5
    
if n != 0:
    result += n  * 2
    
    
print(result)