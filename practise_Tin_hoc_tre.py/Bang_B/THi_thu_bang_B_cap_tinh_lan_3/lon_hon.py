def find_answer(t_list):
    result = "NO"
    if max(t_list) > 1000:
        result = "YES"
    elif t_list[0] + t_list[1] > 1000:
        result = "YES"
    elif t_list[1] + t_list[2] > 1000:
        result = "YES"
    elif t_list[0] + t_list[2] > 1000:
        result = "YES"
    return result
# ------
n = int(input())
my_list = []
for _ in range(n):
    my_list.append(list(map(int, input().split())))

for t_list in my_list:
    print(find_answer(t_list))