row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
k = int(input())
rotes = list(map(int, input().split()))

nums = [row1, row2, row3]

for rote in rotes:
    if rote == 1:
        # a10, a11, a12, a13        a20, a10, a11, a13
        # a20, a21, a22, a23 ==>    a30, a21, a12, a23
        # a30, a31, a32, a33        a31, a32, a22, a33
        tmp = row1[0]
        row1[0] = row2[0]
        row2[0] = row3[0]
        row3[0] = row3[1]
        row3[1] = row3[2]
        row3[2] = row2[2]
        row2[2] = row1[2]
        row1[2] = row1[1]
        row1[1] = tmp
    else:
        # a10, a11, a12, a13        a10, a12, a13, a23
        # a20, a21, a22, a23 ==>    a20, a11, a12, a33
        # a30, a31, a32, a33        a30, a21, a31, a32
        tmp = row1[3]
        row1[3] = row2[3]
        row2[3] = row3[3]
        row3[3] = row3[2]
        row3[2] = row3[1]
        row3[1] = row2[1]
        row2[1] = row1[1]
        row1[1] = row1[2]
        row1[2] = tmp
    
print(' '.join(map(str, row1)))
print(' '.join(map(str, row2)))
print(' '.join(map(str, row3)))