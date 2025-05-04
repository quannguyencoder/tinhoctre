a = int(input())
b = int(input())
n = int(input())
a_n = 0
b_n = 0
_3_n = 3 * n

if a > _3_n:
    a_n = a % _3_n
if b > _3_n:
    b_n = b % _3_n

print("a_n:", a_n)
print("b_n:", b_n)

if a_n > b_n:
    print(a_n - b_n)
elif b_n > a_n:
    print(b_n - a_n)
else:
    print(0)