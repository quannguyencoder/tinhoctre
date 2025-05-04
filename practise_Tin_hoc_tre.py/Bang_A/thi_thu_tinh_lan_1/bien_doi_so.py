N = int(input())
s = list(input())
k = int(input())

if int(s[-1]) % 2 != 0:  
    s[-1] = "0"
    k -= 1

if k > 0 and s[0] != "1":
    s[0] = "1"
    k -= 1

index = 1
max_pos = len(s)
while k > 0 and index < max_pos:
    if s[index] != "0":
        s[index] = "0"
        k -= 1
    index += 1

print(''.join(s))