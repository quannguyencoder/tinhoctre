def count_pair(query):
    b, c = query
    result = 0
    for index in range(n):
        for j in range(index + 1, n):
            if nums[index] + nums[j] == b and nums[index] * nums[j] == c:
                result += 1
    return result

#-----------------------
n = int(input())
nums = list(map(int, input().split()))
q = int(input())
queries = []

for _ in range(q):
    queries.append(list(map(int, input().split()))) # b, c

for query in queries:
    print(count_pair(query))