a = int(input())
t = int(input())
k = int(input())
result = 0

if t >= 59 - a: 
    for item in range (a, 59):
        item = str(item)
        if k in item:
            result += item.count(k)
    
    
else:
    for item in range (a, t + a):
        item = str(item)
        if k in item:
            result += item.count(k)
print(result)