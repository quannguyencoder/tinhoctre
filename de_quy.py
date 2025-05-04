def giaithua(n):
    if n == 0:
        return 1
    
    return n * giaithua(n-1)

print(giaithua(int(input("Ban muon tinh giai thua cua bao nhieu? "))))

# 5! = 5 * 4! = 5 * 4 * 3!