import sys
input = sys.stdin.readline

K, N = map(int, input().split())
have = [int(input()) for _ in range(K)]

def count_lan_cables(length):
    return sum(h // length for h in have)

low, high = 1, max(have)
result = 0

while low <= high:
    mid = (low + high) // 2
    if count_lan_cables(mid) >= N:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
