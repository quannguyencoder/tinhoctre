n = int(input())
cycle = n // 12
total = 0
sum_cycle = (n//12) * 4
remain = 0
if n % 12 >= 11:
    remain += 3
elif n % 12 >= 8:
    remain += 2
elif n % 12 >= 3:
    remain += 1
total = remain + sum_cycle
print(total)