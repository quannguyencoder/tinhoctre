m_n = input()
m_n_list = m_n.split(' ')
m, n = int(m_n_list[0]), int(m_n_list[1])
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k_a = 0
k_b = 0

for index in range (len(a) - 2):
    if a[index] < a[index + 1]:
        k_a += 1
    else:
        break
for index in range (len(b) - 2):
    if a[index] < a[index + 1]:
        k_b += 1
    else:
        break
if k_a > k_b:
    print(k_a + 1)
elif k_b > k_a:
    print(k_b + 1)
else:
    print(k_a + 1)