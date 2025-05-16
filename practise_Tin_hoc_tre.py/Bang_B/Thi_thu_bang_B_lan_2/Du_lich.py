nums = list(map(int, input().split()))
n, l, walk, drive, k = nums
drive_time = l / drive
n -= k
walk_time = n * walk
print(drive_time + walk_time)