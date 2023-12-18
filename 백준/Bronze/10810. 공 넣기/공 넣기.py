import sys

n, m = map(int, input().split())

basket = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for idx in range(i - 1, j):
        basket[idx] = k

result = ' '.join(map(str, basket))
print(result)
