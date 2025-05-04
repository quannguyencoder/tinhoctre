n = int(input())
m = int(input())
k = int(input())
if m % n != 0:
    print((m % n + k - 1) % n)
else:
    print((m % n + k) % n)